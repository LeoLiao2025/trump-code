# 川普密碼 Trump Code — 交接文件
> 日期：2026-03-15
> 專案：trump-code（僅此專案，不涉及其他）
> GitHub：https://github.com/sstklen/trump-code
> 線上：https://trumpcode.washinmura.jp

## 現況一句話
後端 42 個 Python 檔案全部完成 ✅，前端 insights.html 被補了 20+ 次壞掉需要從零重寫 ❌

## 🔴 下個 session 第一件事：從零重寫 insights.html

後端 API 全部 200 OK，前端只要 fetch 就好：
```
GET /api/dashboard    全部數據一次拿
GET /api/status       系統狀態
GET /api/signals      信號+7天歷史
GET /api/models       模型排行
GET /api/polymarket   即時市場
GET /api/data         可下載數據列表
GET /api/data/{file}  下載原始數據
POST /api/chat        聊天
```

### tkman 的 UI 要求（從對話整理）
1. 字體 4 級：L1=36px 數字 / L2=28px 標題 / L3=20px 正文 / L4=16px 輔助
2. 容器寬 1400px，不要斷行
3. 響應式：768px 平板 + 480px 手機
4. 全三語 EN/ZH/JA
5. Trump 配色：金 #FFD700 + 紅 #CC0000 + 海軍藍 #080c18
6. 動態區：🟢 進度條倒數（不是文字）
7. 靜態區：📅 研究期間（2025-01-20~2026-03-15）
8. 首頁=儀表板，/chat=聊天，💬 浮動按鈕
9. 預測市場要有即時數據 + How It Works
10. 信號要有結果（偏多/偏空）
11. Truth Social 全名
12. 字要大，老花眼友善

### 頁面區塊順序
1. Hero（TRUMP CODE 川普密碼）
2. 漏斗（水平 7400→31.5M→550）+ 4 亮點卡
3. Live Status 4 卡片
4. Three Playbooks（避險/佈局/拉盤）
5. Key Discoveries（3 卡 + 8 表格）
6. Dual Platform（Truth Social vs X 5 密碼）
7. Signals & Results（7 天 + 偏多偏空）
8. Model Rankings（11 模型）
9. Architecture（架構圖置中）
10. Prediction Markets（流程 + 數據 + 即時表格）
11. Active Computation（4 引擎）
12. Crowd Insights
13. Open Data（數據目錄 + 下載）
14. Connect（API/CLI/MCP）
15. Footer + 💬

## 後端狀態（全部 OK 不用動）
- 42 個 Python 檔案，17,000+ 行
- 550 條規則，564 筆驗證，61.3% 命中率
- realtime_loop.py（即時引擎，每 5 分鐘）
- daily_pipeline.py（每日管線，11 步）
- learning_engine.py + rule_evolver.py（閉環學習+進化）
- circuit_breaker.py（斷路器+反向規則）
- event_detector.py + dual_platform_signal.py（事件偵測+雙平台）
- polymarket_client.py + kalshi_client.py（預測市場）
- mcp_server.py（9 個 MCP 工具）
- chatbot_server.py（Gemini Flash×3 key + 所有 API）
- VPS systemd service 運行中
- GitHub Actions 每天 UTC 14:00 自動跑

## 另一邊也在改
有另一個終端同時在改這個 repo。見 COLLABORATION.md。不要 force-push。

## 已知問題
- Polymarket 搜尋只找到 GTA VI 類市場，真正的 Trump tariff 市場要用 tag=Trump/Politics
- 系統正在惡化（最近 50% vs 歷史 61%），斷路器在監控
- Kalshi 目前 0 個 Trump 政治市場
