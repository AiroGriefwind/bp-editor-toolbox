import streamlit as st

from ui import CURRENT_TOOL_KEY, TOOL_DIV_REPAIR, TOOL_ITALIC


def _inject_launcher_css() -> None:
    st.markdown(
        """
        <style>
        /* 首頁：五欄列中第 2、第 4 欄為圖磚（避免整行寬條按鈕） */
        div[data-testid="stHorizontalBlock"]:has(div[data-testid="column"]:nth-of-type(5))
            div[data-testid="column"]:nth-of-type(2) .stButton > button,
        div[data-testid="stHorizontalBlock"]:has(div[data-testid="column"]:nth-of-type(5))
            div[data-testid="column"]:nth-of-type(4) .stButton > button {
            width: 168px !important;
            height: 168px !important;
            min-height: 168px !important;
            max-width: 168px !important;
            border-radius: 18px;
            font-size: 1.05rem;
            font-weight: 600;
            white-space: pre-line;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _go(tool: str) -> None:
    st.session_state[CURRENT_TOOL_KEY] = tool
    st.rerun()


def render() -> None:
    _inject_launcher_css()
    st.title("BP 編輯工具箱")
    st.caption("請選擇要使用的工具")

    pad_l, tile1, gap, tile2, pad_r = st.columns([2, 2, 1, 2, 2])
    with pad_l:
        st.empty()
    with tile1:
        if st.button("🔤\n數學斜體", key="tile_italic", use_container_width=True):
            _go(TOOL_ITALIC)
    with gap:
        st.empty()
    with tile2:
        if st.button("🧹\nHTML／div 修復", key="tile_div", use_container_width=True):
            _go(TOOL_DIV_REPAIR)
    with pad_r:
        st.empty()
