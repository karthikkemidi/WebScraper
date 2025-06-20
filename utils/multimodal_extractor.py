import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/119.0.0.0 Safari/537.36"
    )
}

def extract_clean_main_text(url):
    response = requests.get(url, timeout=10, headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(['nav', 'footer', 'header', 'aside', 'script', 'style', 'form', 'noscript']):
        tag.decompose()
    for tag in soup.select('#mw-navigation, #mw-head, #mw-panel, #siteNotice, .mw-jump, .mw-portlet, .vector-menu, .vector-header-container, .vector-footer, .mw-footer'):
        tag.decompose()
    main_content = (
        soup.find('div', {'id': 'bodyContent'}) or
        soup.find('main') or
        soup.find('article') or
        soup
    )
    text = main_content.get_text(separator=" ", strip=True)
    return text[:8000]

def extract_image_urls(url):
    response = requests.get(url, timeout=10, headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    image_tags = soup.find_all("img")
    image_urls = []
    for img in image_tags:
        img_url = img.get("src") or img.get("data-src")
        if img_url:
            full_url = urljoin(url, img_url)
            image_urls.append(full_url)
    return image_urls
