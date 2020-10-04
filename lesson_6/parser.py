import requests
from bs4 import BeautifulSoup

URL = "https://sinoptik.ua/"
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 '
                         'Safari/537.36'}

your_city = input("Введите город, на кирилице: ")
your_date = input("Введите дату поиска\n"
                  "В формате 'гггг-мм-дд': ")


def get_html(url):
    r = requests.get(url)
    return r


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    item = soup.find_all("div", class_="main loaded")

    weather = []
    for it in item:
        weather.append({
            "day": it.find("p", class_="date").get_text(strip=True),
            "month": it.find("p", class_="month").get_text(strip=True),
            "weather": it.find("div", class_="weatherIco").get("title"),
            "min_temp": it.find("div", class_="min").get_text(strip=True),
            "max_temp": it.find("div", class_="max").get_text(strip=True)
        })
    return weather


def parse():
    html = get_html(f"{URL + 'погода-' + your_city + '/' + your_date}")
    if html.status_code == 200:
        get_content(html.text)
    elif html.status_code == 404:
        print("error 404")
    else:
        print("something went wrong")


parse()
