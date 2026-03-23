#!/usr/bin/env python3
"""
Discord 每日通知腳本 — 供 GitHub Actions 呼叫
讀取 daily_report.json + opus_analysis.json → 發送 Discord embed
"""
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).parent.parent
DATA = BASE / "data"


def main():
    webhook = os.environ.get("DISCORD_WEBHOOK_URL", "")
    if not webhook:
        print("DISCORD_WEBHOOK_URL 未設定，跳過通知")
        sys.exit(0)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    report = {}
    analysis = {}
    try:
        report = json.loads((DATA / "daily_report.json").read_text(encoding="utf-8"))
    except Exception:
        pass
    try:
        analysis = json.loads((DATA / "opus_analysis.json").read_text(encoding="utf-8"))
    except Exception:
        pass

    posts_today = report.get("posts_today", report.get("today_posts", "?"))
    signals = report.get("signals", report.get("detected_signals", []))
    signals_str = ", ".join(signals) if isinstance(signals, list) and signals else str(signals) or "無"

    pred = analysis.get("today_prediction", {})
    direction = pred.get("direction", "?")
    confidence = pred.get("confidence", "?")
    hold_days = pred.get("hold_days", "?")
    note = pred.get("note", "")
    health = analysis.get("system_health", {}).get("score", "?")

    dir_emoji = {"LONG": "📈", "SHORT": "📉", "HOLD": "⏸️"}.get(direction, "❓")
    color = {"LONG": 5763719, "SHORT": 15548997}.get(direction, 8421504)

    payload = {
        "embeds": [{
            "title": f"📊 川普密碼 日報 — {today}",
            "color": color,
            "fields": [
                {"name": "今日推文", "value": str(posts_today), "inline": True},
                {"name": "偵測信號", "value": signals_str, "inline": True},
                {"name": "系統健康度", "value": str(health), "inline": True},
                {"name": f"預測方向 {dir_emoji}", "value": f"**{direction}** {hold_days}天", "inline": True},
                {"name": "信心度", "value": str(confidence), "inline": True},
                {"name": "分析說明", "value": (note[:200] if note else "—"), "inline": False},
            ],
            "footer": {"text": "川普密碼 自動分析系統"},
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }]
    }

    req = urllib.request.Request(
        webhook,
        data=json.dumps(payload).encode(),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "TrumpCodeBot/1.0",
        },
    )
    try:
        urllib.request.urlopen(req, timeout=10)
        print("✅ Discord 通知已發送")
    except urllib.error.HTTPError as e:
        print(f"❌ Discord 發送失敗 {e.code}：{e.read().decode()}")
        sys.exit(1)


if __name__ == "__main__":
    main()
