import re

from bs4 import BeautifulSoup


def clean_html(html: str) -> str:
    if not html:
        return ""

    html = re.sub(r"<\s*div(\s+[^>]*)?>", r"<p\1>", html, flags=re.IGNORECASE)
    html = re.sub(r"</\s*div\s*>", "</p>", html, flags=re.IGNORECASE)

    html = re.sub(r"<\s*i(\s+[^>]*)?>", r"<em\1>", html, flags=re.IGNORECASE)
    html = re.sub(r"</\s*i\s*>", "</em>", html, flags=re.IGNORECASE)

    soup = BeautifulSoup(html, "html.parser")

    for h4 in soup.find_all("h4"):
        new_p = soup.new_tag("p")
        new_strong = soup.new_tag("strong")
        for child in list(h4.contents):
            new_strong.append(child)
        new_p.append(new_strong)
        h4.replace_with(new_p)

    for p in soup.find_all("p"):
        text = (p.get_text() or "").strip()
        text_no_nbsp = text.replace("\xa0", "").replace("&nbsp;", "").strip()
        if not text_no_nbsp and not p.find(True):
            p.decompose()

    cleaned = str(soup)
    return cleaned.strip()
