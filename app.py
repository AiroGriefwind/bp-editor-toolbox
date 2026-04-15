import streamlit as st

from ui import CURRENT_TOOL_KEY, TOOL_DIV_REPAIR, TOOL_HOME, TOOL_ITALIC
from ui import div_repair_tool, home, italic_tool


def main() -> None:
    st.set_page_config(page_title="BP 編輯工具箱", layout="wide", page_icon="🧰")

    if CURRENT_TOOL_KEY not in st.session_state:
        st.session_state[CURRENT_TOOL_KEY] = TOOL_HOME

    tool = st.session_state[CURRENT_TOOL_KEY]
    if tool == TOOL_ITALIC:
        italic_tool.render()
    elif tool == TOOL_DIV_REPAIR:
        div_repair_tool.render()
    else:
        home.render()


if __name__ == "__main__":
    main()
