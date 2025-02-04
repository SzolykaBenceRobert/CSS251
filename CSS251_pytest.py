import pytest
from bs4 import BeautifulSoup

def load_html():
    with open("CSS251.html", "r", encoding="utf-8") as file:
        return file.read()

def test_title():
    soup = BeautifulSoup(load_html(), "html.parser")
    assert soup.title.string == "Hajó"

def test_headings():
    soup = BeautifulSoup(load_html(), "html.parser")
    h1 = soup.find("h1")
    h2 = soup.find("h2")
    assert h1 is not None and h1.text == "Hajó"
    assert h2 is not None and h2.text == "A hajó felépítése"

def test_list_items():
    soup = BeautifulSoup(load_html(), "html.parser")
    items = [li.text for li in soup.find_all("li")]
    expected_items = [
        "kémény", "tat", "hajócsavar", "hajótest", "horgony", "bulbaorr", "orr",
        "fedélzet", "hajóúr", "hajóító", "fedélköz", "hajókamera"
    ]
    assert all(item in items for item in expected_items)

def test_styles():
    soup = BeautifulSoup(load_html(), "html.parser")
    h1 = soup.find("h1")
    h2 = soup.find("h2")
    assert "color: red;" in h1.attrs.get("style", "")
    assert "color: green;" in h2.attrs.get("style", "")

