import streamlit as st

from ui import CURRENT_TOOL_KEY, TOOL_HOME
from utils.math_italic import to_math_italic_entities

_ITALIC_RESULT_KEY = "italic_result"


def render() -> None:
    if st.button("← 返回首頁"):
        st.session_state[CURRENT_TOOL_KEY] = TOOL_HOME
        st.rerun()

    st.title("英文字母 → Mathematical Italic（Unicode 實體）")
    st.write("輸入英文文本，按下「開始轉換」後輸出對應的數學斜體 Unicode 實體編碼。")

    if _ITALIC_RESULT_KEY not in st.session_state:
        st.session_state[_ITALIC_RESULT_KEY] = ""

    with st.form("italic_form"):
        input_text = st.text_input(
            "輸入英文文本",
            placeholder="例如：GoGlobal",
            key="italic_form_input",
        )
        submitted = st.form_submit_button("開始轉換", type="primary")

    if submitted:
        st.session_state[_ITALIC_RESULT_KEY] = to_math_italic_entities(input_text)

    st.text_area(
        "輸出（Unicode 實體）",
        value=st.session_state[_ITALIC_RESULT_KEY],
        height=160,
    )
