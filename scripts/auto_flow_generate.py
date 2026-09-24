#!/usr/bin/env python3
"""
Google Flow 静态画格全自动批量生成器 (0 积分 Nano Banana 2)
- 混合驱动：DOM ProseMirror 填充 + bsk 原生 CDP 点击触发
- 集合差分：精确抓取全新生成的 4:3 高清无损画格 URL 并直接落盘
- 自动断点续传：已存在的分镜自动跳过
- 实时同步项目 meta.json 进度
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.project_base import resolve_project


def bsk_eval(session_id: str, code: str, timeout: int = 30) -> str:
    """在 bsk 会话中执行 JavaScript 并返回标准输出"""
    cmd = ["bsk", "evaluate", "--session", session_id, "--timeout", f"{timeout}s", code]
    env = os.environ.copy()
    env["BSK_AUTO_START"] = "0"
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    if res.returncode != 0:
        return f"__ERROR__: {res.stderr.strip()}"
    return res.stdout.strip()


def get_flow_image_urls(session_id: str) -> list:
    """获取当前页面中所有已存在的 flow 高清图片 URL"""
    js = """
(() => {
  const imgs = Array.from(document.querySelectorAll('img')).filter(img => {
    const src = img.currentSrc || img.src || '';
    return src.includes('flow-content.google') && ((img.naturalWidth || img.width) >= 256);
  });
  const urls = Array.from(new Set(imgs.map(i => i.currentSrc || i.src)));
  return JSON.stringify(urls);
})()
"""
    raw = bsk_eval(session_id, js)
    if raw.startswith("__ERROR__"):
        return []
    try:
        return json.loads(raw)
    except Exception:
        return []


def is_page_thinking(session_id: str) -> bool:
    """检查页面是否正在生成"""
    js = """
(() => {
  const stopBtn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.includes('停止'));
  const thinking = document.querySelector('[aria-label="正在思考"], mat-progress-spinner, [class*="thinking"]');
  return !!stopBtn || !!thinking;
})()
"""
    raw = bsk_eval(session_id, js)
    return raw == "true"


def fill_prompt_and_click(session_id: str, prompt_text: str) -> bool:
    """使用 ProseMirror 写入提示词，并通过 bsk observe + bsk click 触发生成"""
    escaped_prompt = json.dumps(prompt_text)
    js_fill = f"""
(() => {{
  const pm = document.querySelector('.ProseMirror');
  if (!pm) return 'no_pm';
  pm.focus();
  document.execCommand('selectAll', false, null);
  document.execCommand('insertText', false, {escaped_prompt});
  pm.dispatchEvent(new InputEvent('input', {{ bubbles: true, cancelable: true, inputType: 'insertText' }}));
  return 'ok';
}})()
"""
    res_fill = bsk_eval(session_id, js_fill)
    if res_fill != "ok":
        print(f"     [错误] 提示词注入失败: {res_fill}")
        return False

    time.sleep(1)

    # 循环等待可点击的“开始生成”按钮出现（防止上一张图还在“停止”收尾阶段）
    env = os.environ.copy()
    env["BSK_AUTO_START"] = "0"
    btn_ref = None
    for attempt in range(12):
        obs = subprocess.run(["bsk", "observe", "--session", session_id], capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
        matches = re.findall(r'(@e\d+)\s+button\s+"开始生成"(?!\s*\[disabled\])', obs.stdout)
        if not matches:
            matches = re.findall(r'(@e\d+)\s+button.*开始生成(?!\s*\[disabled\])', obs.stdout)
        if matches:
            btn_ref = matches[-1]
            break
        time.sleep(2.5)

    if not btn_ref:
        print(f"     [错误] 未找到可点击的“开始生成”按钮！页面观察输出片段:\n{obs.stdout[-500:]}", flush=True)
        return False

    click_res = subprocess.run(["bsk", "click", "--ref", btn_ref, "--session", session_id], capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    if "click ok" in click_res.stdout or click_res.returncode == 0:
        return True

    print(f"     [错误] 点击按钮失败: {click_res.stderr.strip() or click_res.stdout.strip()}", flush=True)
    return False


def download_url(url: str, target_path: Path) -> bool:
    """从 Google CDN 直接下载高清图片并落盘"""
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
            if len(data) < 50000:
                print(f"     [错误] 下载数据异常偏小: {len(data)} 字节", flush=True)
                return False
            target_path.parent.mkdir(parents=True, exist_ok=True)
            with open(target_path, "wb") as f:
                f.write(data)
            return True
    except Exception as e:
        print(f"     [重试] urllib.request 失败 ({e})，尝试 urlretrieve...", flush=True)
        try:
            target_path.parent.mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(url, str(target_path))
            return target_path.exists() and target_path.stat().st_size > 50000
        except Exception as e2:
            print(f"     [错误] 下载图片异常: {e2}", flush=True)
            return False


def generate_panel(session_id: str, panel_idx: int, prompt_text: str, project, max_wait: int = 90):
    """为指定分镜执行提交、等待并保存"""
    out_filename = f"panel_{panel_idx:02d}.png"
    target_path = project.file("04_raw_panels", out_filename)

    print(f"\n[{panel_idx:02d}] 🚀 开始生成分镜: {out_filename}", flush=True)
    print(f"     提示词: {prompt_text[:75]}...", flush=True)

    existing_urls = set(get_flow_image_urls(session_id))

    # 提交并点击开始生成
    ok = fill_prompt_and_click(session_id, prompt_text)
    if not ok:
        return False

    print(f"[{panel_idx:02d}] ⏳ 任务已提交，等待 Nano Banana 2 渲染 (0 积分)...", flush=True)
    start_time = time.time()
    time.sleep(4)  # 等待后端响应进入生成态

    target_url = None
    while time.time() - start_time < max_wait:
        curr_urls = get_flow_image_urls(session_id)
        new_urls = [u for u in curr_urls if u not in existing_urls]
        thinking = is_page_thinking(session_id)

        if new_urls and not thinking:
            target_url = new_urls[-1]
            break

        time.sleep(2)

    if not target_url:
        curr_urls = get_flow_image_urls(session_id)
        new_urls = [u for u in curr_urls if u not in existing_urls]
        if new_urls:
            target_url = new_urls[-1]

    if not target_url:
        print(f"[{panel_idx:02d}] ❌ 等待生成超时，未获取到新生成的画格 URL", flush=True)
        return False

    # 直接从 CDN 下载入库
    dl_ok = download_url(target_url, target_path)
    if dl_ok and target_path.exists():
        size_kb = target_path.stat().st_size / 1024
        print(f"[{panel_idx:02d}] ✅ 成功落盘: {out_filename} ({size_kb:.1f} KB)", flush=True)
        project.record_panel(panel_idx)
        return True
    else:
        print(f"[{panel_idx:02d}] ❌ 下载落盘失败", flush=True)
        return False


def main():
    parser = argparse.ArgumentParser(description="自动驱动 Google Flow 批量生成漫画静态分镜")
    parser.add_argument("--session", "-s", required=True, help="bsk 会话标识符")
    parser.add_argument("--project", "-p", required=True, help="项目名称/slug")
    parser.add_argument("--start", type=int, default=1, help="起始分镜编号 (默认: 1)")
    parser.add_argument("--end", type=int, default=None, help="结束分镜编号 (默认全部分镜)")
    parser.add_argument("--force", action="store_true", help="强制重新生成已存在的分镜")
    args = parser.parse_args()

    project = resolve_project(args.project)
    prompts_dir = project.file("03_panel_prompts")
    prompt_files = sorted(prompts_dir.glob("panel_*.txt"))
    if not prompt_files:
        print(f"[错误] 未在 {prompts_dir} 中找到任何提示词文件！")
        sys.exit(1)

    total_panels = len(prompt_files)
    start_idx = max(1, args.start)
    end_idx = args.end if args.end is not None else total_panels

    print("=" * 65)
    print(f"🎨 Google Flow 自动批量分镜生成器 (0 积分 Nano Banana 2)")
    print(f"📁 项目: {project.slug}")
    print(f"🎯 范围: Panel {start_idx:02d} ~ Panel {end_idx:02d} (共 {end_idx - start_idx + 1} 个分镜)")
    print("=" * 65)

    # 清理之前残留的重复图片（panel_03~12，因为之前可能抓取了重复的 panel_01）
    for p in range(2, 13):
        f = project.file("04_raw_panels", f"panel_{p:02d}.png")
        p01 = project.file("04_raw_panels", "panel_01.png")
        if f.exists() and p01.exists() and f.stat().st_size == p01.stat().st_size:
            f.unlink()

    success_count = 0
    for idx in range(start_idx, end_idx + 1):
        p_file = prompts_dir / f"panel_{idx:02d}.txt"
        if not p_file.exists():
            print(f"[{idx:02d}] ⚠️ 提示词文件不存在: {p_file.name}，跳过")
            continue

        raw_panel = project.file("04_raw_panels", f"panel_{idx:02d}.png")
        if raw_panel.exists() and raw_panel.stat().st_size > 50000 and not args.force:
            print(f"[{idx:02d}] ⏩ 已存在且尺寸正常 ({raw_panel.stat().st_size / 1024:.1f} KB)，跳过 (使用 --force 可覆盖)")
            success_count += 1
            continue

        prompt_text = p_file.read_text(encoding="utf-8").strip()
        ok = generate_panel(args.session, idx, prompt_text, project)
        if ok:
            success_count += 1
        time.sleep(2)

    print("\n" + "=" * 65)
    print(f"🎉 批量生成完毕: 成功 {success_count}/{end_idx - start_idx + 1} 个分镜")
    print(f"📁 输出目录: {project.file('04_raw_panels')}")
    print("=" * 65)


if __name__ == "__main__":
    main()
