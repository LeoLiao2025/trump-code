# 交接文件
> 日期：2026-03-16 | 摘要：前端從零重寫 + 語言切換 + Polymarket API + GitHub 全面更新

## 已完成
- [x] 前端 insights.html 從零重寫 — 1,450+ 行，乾淨 CSS、Inter 字型、3 個響應式斷點
- [x] i18n 語言切換 EN/中/日 — 174 組三語文字，左上角按鈕切換，localStorage 記住選擇
- [x] Polymarket 接上正確 API — 用 `/public-search` 端點（官方文件確認），316 個 Trump 市場
- [x] 後端新增 `/api/recent-posts` — 最近 20 篇川普推文 + 信號分析
- [x] 後端新增 `/api/polymarket-trump` — 即時搜尋 Polymarket Trump 市場
- [x] GitHub README 重寫 — 純英文主版 + docs/README.zh.md + docs/README.ja.md
- [x] GitHub Discussions 開通 — 5 個討論帖（自我介紹/預測/策略/展示/公告）
- [x] Buy Me a Claude Max — 官網右上角+Footer+GitHub 三語 README
- [x] 清理多餘檔案 — 刪掉 10 個（FIXSPEC/COLLABORATION/handoff/重複data）
- [x] 部署到 VPS — trumpcode.washinmura.jp 全功能上線
- [x] X 推文文案 — 三語版 + @mentions + 排程建議

## 已知問題
- Gamma API 的 `slug_contains` 和 `tag_slug` 搜尋壞掉（回傳 GTA VI 垃圾），已改用 `public-search`
- 系統健康狀態 `needs_attention`（最近命中率 50% vs 歷史 61%，斷路器在監控）
- Kalshi 目前 0 個 Trump 政治市場
- 根目錄 43 個 Python 檔案很亂，但決定暫不整理（怕改 import 影響線上服務）

## 下一步（按優先順序）
1. 發 X 推文 — 中文現在可發，日文明天中午 12 點，英文明天晚上 10 點（日本時間）
2. 檔案結構整理 — 等推廣穩定後，把 40 個 .py 搬進 analysis/ engines/ clients/ tools/
3. Polymarket 數據快取 — 目前每次前端載入都即時搜 API，可加 5 分鐘快取降低延遲
4. 川普推文獨立公開 API — 讓外部開發者直接用 `/api/data/trump_posts_all.json` 下載

## 重要連結
- 線上：https://trumpcode.washinmura.jp
- GitHub：https://github.com/sstklen/trump-code
- Discussions：https://github.com/sstklen/trump-code/discussions
- VPS 路徑：/home/ubuntu/trump-code/
- 服務進程：`python3 chatbot_server.py`（直接跑，非 Docker）
