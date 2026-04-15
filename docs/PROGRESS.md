# 项目进度与变更记录

> 建议在每次 **push** 或合并前追加一条，便于 LLM 与同事快速了解最近改动。

---

## 模板（复制使用）

**日期**：YYYY-MM-DD  
**摘要**：一句话说明本次目标。  
**改动**：

- 文件或模块：做了什么

**状态**：进行中 / 已完成  
**已知问题**：（可选）

---

## 2026-04-15 — 模块化与双工具上线

**摘要**：从单文件 `app.py` 拆分为薄入口 + `ui/` + `utils/`，增加首页启动器与 HTML 清理工具。

**改动**：

- `app.py`：仅负责 `set_page_config` 与按 `session_state["current_tool"]` 分发页面。
- `utils/math_italic.py`：数学斜体映射与 `to_math_italic_entities`。
- `utils/html_cleaner.py`：`clean_html`（div→p、h4→p+strong、i→em、删空 p）。
- `ui/home.py`：方形网格入口，进入斜体或 div 修复工具。
- `ui/italic_tool.py`、`ui/div_repair_tool.py`：各工具界面与返回首页。
- `requirements.txt`：声明 `streamlit`、`beautifulsoup4`。
- `docs/PRD.md`、`docs/PROGRESS.md`：产品与进度文档骨架。

**状态**：已完成（本迭代）  
**已知问题**：启动器样式依赖 Streamlit 默认 DOM，大版本升级时若选择器失效需微调 CSS。

---

## 2026-04-15（續）— BP 編輯工具箱 UX、表單觸發與遠端

**摘要**：修正 `TOOL_HOME` 匯入錯誤；工具改為「開始轉換」表單提交；首頁改窄欄＋方塊按鈕樣式；全站 UI 中文改繁體、標題改為「BP 編輯工具箱」；移除 HTML 工具底部部署說明；程式碼推送到 [bp-editor-toolbox](https://github.com/AiroGriefwind/bp-editor-toolbox)。

**改動**：

- `app.py`：`page_title` 改為「BP 編輯工具箱」；補齊 `TOOL_HOME` 匯入。
- `ui/home.py`：標題／說明改繁體；`st.columns([2,2,1,2,2])` 佈局；以 CSS `:has`／`nth-of-type` 固定圖磚按鈕約 168×168。
- `ui/italic_tool.py`：`st.form` +「開始轉換」後才寫入輸出；文案改繁體。
- `ui/div_repair_tool.py`：左欄表單 +「開始轉換」後才計算右欄；刪除 Streamlit Cloud 部署提示；文案改繁體。
- `.gitignore`：忽略 `__pycache__`、常見虛擬環境與本機 secrets。
- `git remote`：`origin` 改指向 `https://github.com/AiroGriefwind/bp-editor-toolbox.git`（由原先 `mathematical-italic` 遷移）。

**狀態**：已完成（本迭代）  
**已知問題**：若瀏覽器不支援 CSS `:has`，首頁圖磚固定寬高可能略弱，仍保有窄欄佈局。
