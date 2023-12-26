#Название концерта, Дата, Время проведения, Место проведения, Цена билета (если указана), Ссылка на подробную информацию о концерте
from bs4 import BeautifulSoup
import json
import urllib3


def found_inf(url: str) -> None:
    count = 1
    dictionary = dict()
    while True:
        text2 = urllib3.request(method='get', url=f'https://{url}.ticketland.ru/concert/page-{count}').data.decode('utf-8')
        soup = BeautifulSoup(text2, 'lxml')
        if soup.find('p', class_='card-search__price') == None or count > 50:
            break
        block = soup.find('div', class_="col-xs-12 col-sm-8 col-lg-9 p-0 p-sm-3").find_all('div',class_="card-search card-search--show")
        for i in block:
            try:
                name = i.find('a', class_="card-search__name").text
                date = i.find('a', class_='text-uppercase').text.split('•')[0]
                time_ = i.find('span', class_='d-none d-sm-inline').text.replace('•', '')
                place = i.find('a', class_="card-search__building text-anchor text-truncate")['title']
                price = i.find('p', class_='card-search__price').text
                link = f"{url}/" + str(i.find('a', class_="btn btn--primary d-block")['href'])
            except TypeError:
                print(f"[-] {count} {i.find('a', class_='card-search__name').text}")
            except AttributeError:
                print(f"[-] {count} {i.find('a', class_='card-search__name').text}")
            else:
                print(f"[+] {count} {i.find('a', class_='card-search__name').text}".replace('\n', '').replace('\t', ''))
                dictionary[name.replace('\n', '').replace('\t', '').replace(' ', '')] = {
                    'name': name.replace('\n', '').replace('\t', '').replace(' ', ''),
                    'date': date.replace('\n', '').replace('\t', '').replace(' ', ''),
                    'time': time_.replace('\n', '').replace('\t', '').replace(' ', ''),
                    'place': place.replace('\n', '').replace('\t', '').replace(' ', ''),
                    'price': price.replace('\n', '').replace('\t', '').replace(' ', ''),
                    'link': link.replace('\n', '').replace('\t', '').replace(' ', ''),
                }
        count += 1
    with open(f"{url}.json", "a+", encoding='utf-8') as file:
        json.dump(dictionary, file, indent=4, ensure_ascii=False)
