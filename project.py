source = 'https://ads.vk.com/cases'
source_saved = "C:/Users/lenna/Downloads/Кейсы по таргетированной рекламе — VK Реклама.html"
import requests
from bs4 import BeautifulSoup


'''
response = requests.get(source)
soup = BeautifulSoup(response.text, "html.parser")
'''
with open(source_saved, "r", encoding="utf-8") as f:
    html = f.read()
    soup = BeautifulSoup(html, 'html.parser')

# выбор карточек
soup.find(class_="pages_content__ycGet")
cards = soup.select("a[class^='case-card_wrapper__']")

results = []

for card in cards:
    # ссылка на кейс
    href = card.get("href")

    # заголовок
    title_div = card.select_one("div[itemprop='headline']")
    title = title_div.text.strip()
    

    # дата
    date_div = card.select_one("div[class^='case-card_date__']")
    date = date_div.get_text(strip=True)

    results.append({
        "заголовок": title,
        "ссылка": source[:-6]+href,
        "дата публикации": date
    })

for idx, item in enumerate(results, 1):
    print(f"\n--- Result {idx} ---")
    for key, value in item.items():
        print(f"{key}: {value}")
