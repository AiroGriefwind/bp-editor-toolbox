import string

import streamlit as st


def build_math_italic_map() -> dict[str, str]:
    upper_codes = [0x1D434 + i for i in range(26)]
    lower_codes = [
        0x1D44E,  # a
        0x1D44F,  # b
        0x1D450,  # c
        0x1D451,  # d
        0x1D452,  # e
        0x1D453,  # f
        0x1D454,  # g
        0x210E,   # h (Planck constant symbol used for math italic h)
        0x1D456,  # i
        0x1D457,  # j
        0x1D458,  # k
        0x1D459,  # l
        0x1D45A,  # m
        0x1D45B,  # n
        0x1D45C,  # o
        0x1D45D,  # p
        0x1D45E,  # q
        0x1D45F,  # r
        0x1D460,  # s
        0x1D461,  # t
        0x1D462,  # u
        0x1D463,  # v
        0x1D464,  # w
        0x1D465,  # x
        0x1D466,  # y
        0x1D467,  # z
    ]

    mapping: dict[str, str] = {}
    for ch, code in zip(string.ascii_uppercase, upper_codes):
        mapping[ch] = f"&#x{code:X};"
    for ch, code in zip(string.ascii_lowercase, lower_codes):
        mapping[ch] = f"&#x{code:X};"
    return mapping


MATH_ITALIC_MAP = build_math_italic_map()


def to_math_italic_entities(text: str) -> str:
    return "".join(MATH_ITALIC_MAP.get(ch, ch) for ch in text)


st.set_page_config(page_title="Mathematical Italic 转换器", page_icon="🔤")
st.title("英文字母 → Mathematical Italic（Unicode 实体）")
st.write("输入英文文本，输出对应的数学斜体 Unicode 实体编码。")

input_text = st.text_input("输入英文文本", value="", placeholder="例如: GoGlobal")
output_text = to_math_italic_entities(input_text)

st.text_area("输出（Unicode 实体）", value=output_text, height=160)
