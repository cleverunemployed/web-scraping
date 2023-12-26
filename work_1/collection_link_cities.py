from bs4 import BeautifulSoup
import json
import urllib3


def find_cities() -> None:

    text = urllib3.request('GET', "https://bryansk.ticketland.ru/").data.decode('utf-8')
    soup = BeautifulSoup(text, 'lxml')
    block = soup.find('ul', class_="dropdown__list").find_all('li')

    dictionary = dict()

    for i in block:
        link = str(i["data-js-dd-item"]).replace('changesd', '').replace('/', '')
        data = str(i.text).replace('\n','').replace('  ','').lower()
        dictionary[data] = link

    with open("data.json", "w", encoding='utf-8') as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=4)