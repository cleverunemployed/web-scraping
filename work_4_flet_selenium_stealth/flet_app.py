# -*- coding: utf-8
import flet as ft
import time
import csv
import os
import pandas as pd
from bs4 import BeautifulSoup
from selenium_stealth import stealth
from selenium import webdriver
from selenium.webdriver.common.by import By


list_sud: list = [
    "Высший Арбитражный Суд РФ",
    "АС Волго - Вятского округа",
    "АС Восточно - Сибирского округа",
    "АС Дальневосточного округа",
    "АС Западно - Сибирского округа",
    "АС Московского округа",
    "АС Поволжского округа",
    "АС Северо - Западного округа",
    "АС Северо - Кавказского округа",
    "АС Уральского округа",
    "АС Центрального округа",
    "1 арбитражный апелляционный суд",
    "2 арбитражный апелляционный суд",
    "3 арбитражный апелляционный суд",
    "4 арбитражный апелляционный суд",
    "5 арбитражный апелляционный суд",
    "6 арбитражный апелляционный суд",
    "7 арбитражный апелляционный суд",
    "8 арбитражный апелляционный суд",
    "9 арбитражный апелляционный суд",
    "10 арбитражный апелляционный суд",
    "11 арбитражный апелляционный суд",
    "12 арбитражный апелляционный суд",
    "13 арбитражный апелляционный суд",
    "14 арбитражный апелляционный суд",
    "15 арбитражный апелляционный суд",
    "16 арбитражный апелляционный суд",
    "17 арбитражный апелляционный суд",
    "18 арбитражный апелляционный суд",
    "19 арбитражный апелляционный суд",
    "20 арбитражный апелляционный суд",
    "21 арбитражный апелляционный суд",
    "АС Алтайского края",
    "АС Амурской области",
    "АС Архангельской области",
    "АС Астраханской области",
    "АС Белгородской области",
    "АС Брянской области",
    "АС Владимирской области",
    "АС Волгоградской области",
    "АС Вологодской области",
    "АС Воронежской области",
    "АС города Москвы",
    "АС города Санкт - Петербурга и Ленинградской области",
    "АС города Севастополя",
    "АС Донецкой Народной Республики",
    "АС Еврейской автономной области",
    "АС Забайкальского края",
    "АС Запорожской области",
    "АС Ивановской области",
    "АС Иркутской области",
    "АС Кабардино - Балкарской Республики",
    "АС Калининградской области",
    "АС Калужской области",
    "АС Камчатского края",
    "АС Карачаево - Черкесской Республики",
    "АС Кемеровской области",
    "АС Кировской области",
    "АС Коми - Пермяцкого АО",
    "АС Костромской области",
    "АС Краснодарского края",
    "АС Красноярского края",
    "АС Курганской области",
    "АС Курской области",
    "АС Липецкой области",
    "АС Луганской Народной Республики",
    "АС Магаданской области",
    "АС Московской области",
    "АС Мурманской области",
    "АС Нижегородской области",
    "АС Новгородской области",
    "АС Новосибирской области",
    "АС Омской области",
    "АС Оренбургской области",
    "АС Орловской области",
    "АС Пензенской области",
    "АС Пермского края",
    "АС Приморского края",
    "АС Псковской области",
    "АС Республики Адыгея",
    "АС Республики Алтай",
    "АС Республики Башкортостан",
    "АС Республики Бурятия",
    "АС Республики Дагестан",
    "АС Республики Ингушетия",
    "АС Республики Калмыкия",
    "АС Республики Карелия",
    "АС Республики Коми",
    "АС Республики Крым",
    "АС Республики Марий Эл",
    "АС Республики Мордовия",
    "АС Республики Саха",
    "АС Республики Северная Осетия",
    "АС Республики Татарстан",
    "АС Республики Тыва",
    "АС Республики Хакасия",
    "АС Ростовской области",
    "АС Рязанской области",
    "АС Самарской области",
    "АС Саратовской области",
    "АС Сахалинской области",
    "АС Свердловской области",
    "АС Смоленской области",
    "АС Ставропольского края",
    "АС Тамбовской области",
    "АС Тверской области",
    "АС Томской области",
    "АС Тульской области",
    "АС Тюменской области",
    "АС Удмуртской Республики",
    "АС Ульяновской области",
    "АС Хабаровского края",
    "АС Ханты - Мансийского АО",
    "АС Херсонской области",
    "АС Челябинской области",
    "АС Чеченской Республики",
    "АС Чувашской Республики",
    "АС Чукотского АО",
    "АС Ямало - Ненецкого АО",
    "АС Ярославской области",
    "ПСП Арбитражного суда Пермского края",
    "ПСП Арбитражный суд Архангельской области",
    "Суд по интеллектуальным правам",
]


result_main: dict = {
    "Участник дела": "",
    "Судья": "",
    "Суд": "",
    "Номер дела": "",
    "дата начало": "",
    "дата конец": "",
}


list_1: list[ft.Row] = []
list_2: list[ft.Row] = []
list_3: list[ft.Row] = []
list_4: list[ft.Row] = []


def start_app(page: ft.Page):

    def anchor_click(e):
        text = f"{e.control.data}"
        result_main["Суд"] = text
        tb3.close_view(text)

    def start_parsing(e):
        result_main["Участник дела"] = str(tb1.value)
        result_main["Судья"] = str(tb2.value)
        result_main["Номер дела"] = str(tb4.value)
        result_main["дата начало"] = str(tb5.value)
        result_main["дата конец"] = str(tb6.value)
        main_parsing(e)

    def main_parsing(e):

        def csv_to_excel():
            new_dataFrame = pd.read_csv('kad.csv', sep=';', encoding='utf-8', quoting=3)
            new_dataFrame.to_excel("SampleExcelFile.xlsx", sheet_name="Subjects", index=False)
            if os.path.isfile("kad.csv"):
                os.remove("kad.csv")

        def alert_final():
            page.snack_bar = ft.SnackBar(ft.Text("Всё ОК!", style=ft.TextStyle(
                color=ft.colors.WHITE,
                size=50
            )), bgcolor=ft.colors.GREEN_300)
            page.snack_bar.open = True
            _status.value = "Загрузка завершена!"
            _status.style.color = ft.colors.GREEN
            csv_to_excel()
            page.update()

        page.clean()
        page.title = "Program"
        page.theme_mode = "light"
        # page.vertical_alignment = ft.MainAxisAlignment.CENTER

        page.window_height = 500
        page.window_width = 390
        page.window_max_height = 500
        page.window_max_width = 390
        page.window_min_height = 500
        page.window_min_width = 390

        page.update()

        _title = ft.Text(value="Ожидайте, идёт парсинг!", scale=2)

        _progress_bar = ft.ProgressBar(bar_height=8, scale=1, bgcolor=ft.colors.WHITE, width=340)

        _status = ft.Text(value="Идёт загрузка!", style=ft.TextStyle(
            color=ft.colors.AMBER,
            size=35,
            font_family="Kanit"
        ))

        _exit_button = ft.TextButton(text="Exit", scale=2, on_click=lambda e: page.window_close(), style=ft.ButtonStyle(
            bgcolor=ft.colors.RED_50
        ))

        page.add(
            ft.Container(
                ft.Stack(
                    [
                        ft.Container(
                            _title,
                            top=10,
                            right=100,
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            _progress_bar,
                            top=95,
                            left=10,
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            _status,
                            top=150,
                            left=50,
                            right=50,
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            _exit_button,
                            top=390,
                            right=40,
                            alignment=ft.alignment.center
                        )
                    ]
                ),
                width=400,
                height=500
            )
        )

    def button_append(value, number, mode=None) -> None:
        if value != "":
            match number:
                case "1":
                    list_1.append(ft.Row([
                        ft.TextField(value=value, disabled=True, width=300),
                        ft.TextField(value=mode, disabled=True, width=100),
                        ft.TextButton(icon=ft.icons.DELETE, icon_color=ft.colors.ORANGE, on_click=lambda e: print("trash"))
                    ], spacing=0))
                case "2":
                    list_2.append(ft.Row([
                        ft.TextField(value=value, disabled=True, width=300),
                        ft.TextButton(icon=ft.icons.DELETE, icon_color=ft.colors.ORANGE, on_click=lambda e: print("trash"))
                    ], spacing=0))
                case "3":
                    list_3.append(ft.Row([
                        ft.TextField(value=value, disabled=True, width=300),
                        ft.TextButton(icon=ft.icons.DELETE, icon_color=ft.colors.ORANGE, on_click=lambda e: print("trash"))
                    ], spacing=0))
                case "4":
                    list_4.append(ft.Row([
                        ft.TextField(value=value, disabled=True, width=300),
                        ft.TextButton(icon=ft.icons.DELETE, icon_color=ft.colors.ORANGE, on_click=lambda e: print("trash"))
                    ], spacing=0))
        page.update()

    def button_cancel(e, number: int) -> None:
        match number:
            case "1":
                list_1.append()
            case "2":
                list_2.append()
            case "3":
                list_3.append()
            case "4":
                list_4.append()
#        try:
#            with open('kad.csv', "a+", newline='', encoding="utf-8") as csvfile:
#                csvwriter = csv.writer(csvfile, delimiter=";")
#                csvwriter.writerow(["Дело", "Ссылка", "Судья | текущая инстанция", "Истец", "Ответчик"])
#                csvfile.close()
#            for i in range(1):
#                try:
#                    options = webdriver.ChromeOptions()
#                    # options.add_argument("start-maximized")
#                    options.add_argument("--headless=new")
#                    options.add_experimental_option("excludeSwitches", ["enable-automation"])
#                    options.add_experimental_option('useAutomationExtension', False)
#                    driver = webdriver.Chrome(options=options)
#                except:
#                    pass
#                else:
#                    break
#            else:
#                options = webdriver.EdgeOptions()
#                # options.add_argument("start-maximized")
#                options.add_argument("--headless=new")
#                options.add_experimental_option("excludeSwitches", ["enable-automation"])
#                options.add_experimental_option('useAutomationExtension', False)
#                driver = webdriver.Edge(options=options)
#
#            stealth(driver=driver,
#                    languages=["ru-RU", "ru"],
#                    vendor="Google Inc.",
#                    platform="Win32",
#                    webgl_vendor="Intel Inc.",
#                    renderer="Intel Iris OpenGL Engine",
#                    fix_hairline=True,
#                    run_on_insecure_origins=True,
#                    )
#
#            driver.get('https://kad.arbitr.ru/')
#            time.sleep(9)
#
#            driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/dl/dd/div[1]/div/textarea').send_keys(result_main["Участник дела"])
#            driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/dl/dd/div[2]/div/input').send_keys(result_main["Судья"])
#            driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/dl/dd/div[3]/div/span/label/input').send_keys(result_main["Суд"])
#            driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/dl/dd/div[4]/div/input').send_keys(result_main["Номер дела"])
#            #driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/dl/dd/div[5]/label[1]/input').send_keys(result_main["дата начало"])
#            #driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/dl/dd/div[5]/label[2]/input').send_keys(result_main["дата конец"])
#            #driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/dl/dd/div[5]/label[2]/input').click()
#            element_2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/dl/dd/div[4]/div/input')
#            driver.execute_script("arguments[0].click();", element_2)
#            time.sleep(9)
#            element = driver.find_element(By.XPATH, '//*[@id="b-form-submit"]/div/button')
#
#            driver.execute_script("arguments[0].click();", element)
#
#            time.sleep(9)
#
#            count: float = 2.5
#
#            while True:
#
#                _progress_bar.value = count * 0.01
#
#                count += 2.5
#                page.update()
#
#                time.sleep(5)
#
#                result: list = []
#
#                soup = BeautifulSoup(driver.page_source, 'lxml')
#
#                blocks = soup.find("div", id="table").find("table", id="b-cases").find("tbody").find_all("tr")
#
#                for block in blocks:
#                    link = str(block.find("td", {"class": "num"}).find("a")["href"]).replace("\n", "").replace("\t", "").replace("   ", "")
#                    title = str(block.find("td", {"class": "num"}).text).replace("\n", "").replace("\t", "").replace("   ", "")
#                    court = str(block.find("td", {"class": "court"}).text).replace("\n", "").replace("\t", "").replace("   ", "")
#                    try:
#                        plaintiff = ', '.join([str(x.text) for x in block.find("td", {"class": "plaintiff"}).find_all("strong") if not str(x.text).isdigit()])
#                    except AttributeError:
#                        plaintiff = ""
#                    try:
#                        respondent = ', '.join([str(x.text) for x in block.find("td", {"class": "respondent"}).find_all("strong") if not str(x.text).isdigit()])
#                    except AttributeError:
#                        respondent = ""
#                    result.append([title, link, court, plaintiff, respondent])
#
#                with open('kad.csv', "a+", newline='', encoding="utf-8") as csvfile:
#                    csvwriter = csv.writer(csvfile, delimiter=";")
#                    csvwriter.writerows(result)
#                    csvfile.close()
#
#                try:
#                    element_3 = driver.find_element(By.CLASS_NAME, "rarr")
#                    driver.execute_script("arguments[0].click();", element_3)
#                    if count == 102.5:
#                        driver.close()
#                        driver.quit()
#                        break
#                except:
#                    driver.close()
#                    driver.quit()
#                    break
#
#            alert_final()
#            page.update()
#        except:
#            _status.value = "Ошибка!"
#            _status.color = ft.colors.RED
#            page.update()



    page.title = "Program"
    page.theme_mode = "light"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.window_height = 500
    page.window_width = 1600
    page.window_max_height = 500
    page.window_max_width = 1600
    page.window_min_height = 500
    page.window_min_width = 1600

    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Open Sans": "/fonts/OpenSans-Regular.ttf",
        "Sunny day": "C:/Users/kassl/Downloads/sunny-day/Sunny-day.ttf"
    }
    page.update()

    tb1 = ft.TextField(label="Участник дела", hint_text="Название, ИНН или ОГРН")
    tb2 = ft.TextField(label="Судья", hint_text="Фамилия судьи")
    tb3 = ft.SearchBar(
        view_elevation=4,
        divider_color=ft.colors.AMBER,
        bar_hint_text="Суд",
        view_hint_text="Название суда",
        width=300,
        controls=[
            ft.ListTile(title=ft.Text(value=f"{i}"), on_click=anchor_click, data=i) for i in list_sud
        ]
    )

    tb4 = ft.TextField(label="Номер дела", hint_text="Например: А50-5568/08")
    #tb5 = ft.TextField(label="Дата регистрации дела", hint_text="дд.мм.гг", width=170)
    #tb6 = ft.TextField(label="Дата регистрации дела", hint_text="дд.мм.гг", width=170)

    mode_tb1 = ft.Dropdown(
        width=100,
        hint_text="Любой",
        disabled=False,
        options=[
            ft.dropdown.Option("Любой"),
            ft.dropdown.Option("Истец"),
            ft.dropdown.Option("Ответчик"),
            ft.dropdown.Option("Третье лицо"),
            ft.dropdown.Option("Иное лицо"),
        ],
    )

    button_plus_1 = ft.TextButton(icon=ft.icons.ADD_CIRCLE, icon_color=ft.colors.BLUE, on_click=button_append(value=tb1.value, number="1", mode=mode_tb1.value))
    button_plus_2 = ft.TextButton(icon=ft.icons.ADD_CIRCLE, icon_color=ft.colors.BLUE, on_click=button_append(value=tb2.value, number="2"))
    button_plus_3 = ft.TextButton(icon=ft.icons.ADD_CIRCLE, icon_color=ft.colors.BLUE, on_click=button_append(value=tb3.value, number="3"))
    button_plus_4 = ft.TextButton(icon=ft.icons.ADD_CIRCLE, icon_color=ft.colors.BLUE, on_click=button_append(value=tb4.value, number="4"))
    button_start = ft.TextButton(text="Start", on_click=start_parsing, style=ft.ButtonStyle(
        bgcolor=ft.colors.CYAN_50
    ))

    button_exit = ft.TextButton(text="Exit", on_click=lambda e: page.window_close(), style=ft.ButtonStyle(
        bgcolor=ft.colors.RED_50
    ))

    main_row = ft.Row([
        tb1, mode_tb1, button_plus_1, tb2, button_plus_2, tb3, button_plus_3, tb4, button_plus_4
    ], spacing=0)

    page.add(
        ft.Container(
            ft.Stack(
                [
                    ft.Container(
                        ft.Stack([
                            ft.Container(
                                main_row,
                                top=0,
                                width=1600,
                                height=60
                            ),
                            ft.Container(
                                ft.Column(
                                    [list_1[i] for i in range(len(list_1))] if len(list_1) > 0 else None
                                ),
                                top=65,
                                height=300,
                                left=0
                            ),
                            ft.Container(
                                ft.Column(
                                    [list_2[i] for i in range(len(list_2))] if len(list_2) > 0 else None
                                ),
                                top=65,
                                height=300,
                                left=460
                            ),
                            ft.Container(
                                ft.Column(
                                    [list_3[i] for i in range(len(list_3))] if len(list_3) > 0 else None
                                ),
                                top=65,
                                height=300,
                                left=820,
                            ),
                            ft.Container(
                                ft.Column(
                                    [list_4[i] for i in range(len(list_4))] if len(list_4) > 0 else None
                                ),
                                top=65,
                                height=300,
                                left=1180
                            ),
                        ])
                    ),

                    ft.Container(
                        button_start,
                        left=30,
                        top=390,
                        scale=2,
                    ),
                    ft.Container(
                        button_exit,
                        right=30,
                        top=390,
                        scale=2,
                    )
                ]
            ),
            width=1600,
            height=500
        )
    )


if __name__ == "__main__":
    ft.app(target=start_app)