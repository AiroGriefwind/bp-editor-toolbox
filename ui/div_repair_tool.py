import streamlit as st

from ui import CURRENT_TOOL_KEY, TOOL_HOME
from utils.html_cleaner import clean_html

_DIV_CLEANED_KEY = "div_cleaned"


def render() -> None:
    if st.button("← 返回首頁"):
        st.session_state[CURRENT_TOOL_KEY] = TOOL_HOME
        st.rerun()

    st.title("HTML div／h4 清理工具")
    st.caption("將 div → p、h4 → strong，並清理空段落")

    if _DIV_CLEANED_KEY not in st.session_state:
        st.session_state[_DIV_CLEANED_KEY] = ""

    col1, col2 = st.columns(2)

    with col1:
        with st.form("div_repair_form"):
            raw_html = st.text_area("原始 HTML", height=440, key="div_repair_raw")
            submitted = st.form_submit_button("開始轉換", type="primary")

    if submitted:
        raw = st.session_state.get("div_repair_raw", "")
        st.session_state[_DIV_CLEANED_KEY] = clean_html(raw) if raw else ""

    with col2:
        st.text_area(
            "處理後 HTML（可複製）",
            value=st.session_state[_DIV_CLEANED_KEY],
            height=500,
        )
