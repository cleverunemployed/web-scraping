import collection_conserts
import collection_link_cities
import json

list_cites: dict = dict()


def print_cities():
    with open('data.json', 'r') as file:
        global list_cites
        list_cites = json.load(file)
    for i in list_cites.keys():
        print(i)


def main() -> None:
    print("Выберите опцию:")
    print("1. Обновить список городов (1)")
    print("2. Найти все концерты В определённом городе.(2)")
    try:
        asnwer: int = int(input("Введите операцию (1 или 2): "))
    except ValueError:
        print("!Введите только цифру!")
        main()
        return
    match asnwer:
        case 1:
            collection_link_cities.find_cities()
            print("[+] Обновлён список городов")
            main()
            return
        case 2:
            print_cities()
            citi: str = input("Введите название города: ").lower()
            if citi not in list_cites.keys():
                print("Неверно введено название города")
                main()
                return
            else:
                print("[+] Поиск начался")
                collection_conserts.found_inf(list_cites[citi])
                print("[+] Поиск закончился")
        case _:
            pass


if __name__ == "__main__":
    main()