from selenium import webdriver

from time import sleep
from bs4 import BeautifulSoup


url: str = "https://www.youtube.com/results?search_query=обучение+wb"

massive: set = set()

def download_page(url: str) -> None:
    driver = webdriver.Edge()
    driver.get(url=url)
    sleep(5)
    with open('html.txt', 'w', encoding='utf-8') as file:
        file.write(driver.page_source)
    driver.quit()


def extraction_page(name_file: str) -> None:
    with open(name_file, "r", encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'lxml')
    block = soup.find_all('a', class_="yt-simple-endpoint style-scope yt-formatted-string")
    for i in block:
        massive.add((i['href'], i.text))
        print(f"[+] {i['href']} ~~~ {i.text}")
    with open('1.txt', 'a+', encoding='utf-8') as file1:
        for j in massive:
            file1.write(f"{j[0]} ~~~ {j[1]}\n")

def main() -> None:
    # download_page(url=url)
    extraction_page('html.txt')


if __name__ == "__main__":
    main()