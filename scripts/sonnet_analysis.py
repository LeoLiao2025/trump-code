#!/usr/bin/env python3
"""
Sonnet 信號分析腳本 — 供 GitHub Actions 呼叫
讀取 data/opus_briefing.txt → 呼叫 Anthropic API → 寫入 data/opus_analysis.json
"""
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).parent.parent
BRIEFING_FILE = BASE / "data" / "opus_briefing.txt"
OUTPUT_FILE = BASE / "data" / "opus_analysis.json"

SYSTEM_PROMPT = """你是川普密碼系統的信號分析師。根據簡報包內容，輸出嚴格的 JSON 格式分析，不要有任何額外文字或 markdown。

必須輸出的 JSON 欄位：
{
  "date": "YYYY-MM-DD",
  "analyzed_at": "ISO8601",
  "analyzed_by": "claude-sonnet-4-6",
  "missed_signals": ["信號1", "信號2"],
  "error_analysis": {"模型名": "根本原因說明"},
  "pattern_shift_detected": true,
  "pattern_changes": ["發現的新模式"],
  "new_rules": [
    {"id": "E1_xxx", "name": "規則名稱", "features": ["feature1"], "direction": "LONG", "hold": 2, "confidence": 0.7}
  ],
  "model_adjustments": {
    "increase_weight": {"模型名": 1.2},
    "decrease_weight": {"模型名": 0.8},
    "eliminate": ["模型名（原因）"]
  },
  "signal_confidence": {"信號名": 0.7},
  "system_health": {
    "score": "70/100",
    "grade": "B",
    "priorities": ["1. 最優先事項", "2. 次優先事項"]
  },
  "today_prediction": {
    "bias": "BULLISH",
    "direction": "LONG",
    "hold_days": 2,
    "confidence": 0.7,
    "active_signals": ["信號1"],
    "suppressing_signals": ["抑制信號"],
    "note": "一句話說明"
  }
}"""


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("❌ ANTHROPIC_API_KEY 未設定，跳過 Sonnet 分析")
        sys.exit(0)

    if not BRIEFING_FILE.exists():
        print(f"❌ {BRIEFING_FILE} 不存在，跳過")
        sys.exit(0)

    briefing = BRIEFING_FILE.read_text(encoding="utf-8")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    payload = json.dumps({
        "model": "claude-sonnet-4-6",
        "max_tokens": 4096,
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": briefing}],
    }).encode()

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read())
            text = data["content"][0]["text"].strip()

            # 清除可能的 markdown code block
            if text.startswith("```"):
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]

            analysis = json.loads(text)
            analysis["date"] = today
            analysis["analyzed_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            OUTPUT_FILE.write_text(json.dumps(analysis, ensure_ascii=False, indent=2), encoding="utf-8")

            pred = analysis.get("today_prediction", {})
            print(f"✅ Sonnet 分析完成 → {OUTPUT_FILE}")
            print(f"   今日預測：{pred.get('direction')} 信心度 {pred.get('confidence')} 持有 {pred.get('hold_days')} 天")

    except urllib.error.HTTPError as e:
        print(f"❌ API 錯誤 {e.code}：{e.read().decode()}")
        sys.exit(1)
    except (json.JSONDecodeError, KeyError) as e:
        print(f"❌ 解析失敗：{e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 分析失敗：{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
