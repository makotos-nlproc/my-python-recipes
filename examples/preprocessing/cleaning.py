from bs4 import BeautifulSoup
import re


def clean_html(html: str, strip=False):
    """HTML文字列からタグを除去した文字列を返す

    strip=Trueで改行文字も除去する

    """
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(strip=strip)
    return text


def clean_pattern(text: str, pattern: str):
    """文字列から正規表現でパターンを除去する

    https://regex101.com/ で細かくパターンを確認しながら調整すると良い

    """

    cleaned_text = re.sub(pattern, "", text)
    return cleaned_text
