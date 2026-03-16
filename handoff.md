# 交接文件
> 日期：2026-03-16 (Session 2) | 摘要：即時引擎三源 + 信號接前端 + Devvit 預測遊戲 App 完工（待部署）

## 已完成

### 即時引擎（VPS 已上線）
- [x] 三源抓取 — CNN + trumpstruth.org + X API，每 5 分鐘掃
- [x] systemd 常駐服務 — `trump-realtime.service`，掛了 30 秒重啟
- [x] 新推文自動寫入網站 — 44,076 篇，前端即時顯示
- [x] Polymarket 快照修復 — /public-search API，390 個市場
- [x] 追蹤窗口延長 — 1h/3h/6h/12h/24h/48h
- [x] X API Bearer Token 更新到 VPS
- [x] 即時信號接回前端 — 每篇推文卡片都有信號標籤（TARIFF 90% 等）
- [x] 遊戲 API 4 端點 — game-signal / game-result / game-leaderboard / game-stats

### Devvit 預測遊戲（本機完成，待部署）
- [x] Devvit CLI 安裝 + 登入（PipeAccording5302）
- [x] 4 張卡全部完成，build 成功
- [x] Server：拉信號 + 建帖 + 投票 + 開獎 + 排行榜 + AI vs Crowd
- [x] 前端：投票按鈕 + 即時比例 + 倒數計時 + 結果面板 + 排行榜頁
- [x] 積分系統：猜對 +10、反 AI +25、猜錯 -5、連勝加成
- [x] devvit.json：2 個 menu items（建帖 + 開獎）

### 其他
- [x] Devvit MCP 設定到 Claude Code（~/.claude/.mcp.json）
- [x] Reddit API 調查 — 被 Responsible Builder Policy 擋，走 Devvit
- [x] 日文版 X 推文文案翻譯

## 進行中
- [ ] Devvit App 部署 — build 好了，需要先建 subreddit 再 `npm run deploy`
- [ ] VPS 遊戲 API 部署 — chatbot_server.py 有新的 4 個端點，需重啟 server

## 已知問題
- Truth Social API 被 Cloudflare 403 擋 — client_id/secret 是佔位符，不影響（CNN+trumpstruth 覆蓋）
- Reddit API 無法自助申請 — 只能走 Devvit
- og:image 還沒做

## 下一步（按優先順序）
1. 建 subreddit — 去 Reddit 建 r/TrumpCodeGame
2. 部署 Devvit — `cd /tmp/trump-code-bot/trumpcode && npm run deploy`
3. 部署 VPS 遊戲 API — `ssh washin 'cd /home/ubuntu/trump-code && git pull && kill $(pgrep -f chatbot_server); nohup python3 chatbot_server.py >> server.log 2>&1 &'`
4. 測試完整流程 — menu 建帖 → 投票 → 6h 後開獎
5. 跟單機器人 — $TRUMP 幣信號→Binance API

## 重要連結
- 線上：https://trumpcode.washinmura.jp
- GitHub：https://github.com/sstklen/trump-code
- VPS 即時引擎：`sudo systemctl status trump-realtime`
- Devvit 專案：/tmp/trump-code-bot/trumpcode/
- Devvit Token：~/.devvit/token
- Reddit 帳號：PipeAccording5302
