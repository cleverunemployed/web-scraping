import requests
from fake_useragent import UserAgent



url_start: str = "https://api.cian.ru/agent-catalog-search/v1/get-realtors/?regionId=1&page="
url_end: str = "&limit=10"


def createFile(url: str) -> None:
    headers: dict = {
        'user': UserAgent().random
    }

    response = requests.get(url=url, headers=headers)
    data = response.json()

    result: list = list()

    for item in data["items"]:
        if "cianUserId" in item:
            result.append(item.get("cianUserId"))
    else:
        with open('html.txt', "a+", encoding='utf-8') as file:
            for i in result:
                file.write('https://www.cian.ru/agents/' + str(i)+'/'+'\n')
 


def main() -> None:
    for i in range(1, 2910):
        url = url_start + str(i) + url_end
        createFile(url=url)
        print(f"[+] Succes download {i}")



if __name__ == "__main__":
    main()