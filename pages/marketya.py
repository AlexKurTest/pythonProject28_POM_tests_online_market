import os
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements

class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://market.yandex.ru/'

        super().__init__(web_driver, url)

    # Главное поле поиска
    search = WebElement(id='header-search')

    # Кнопка поиска
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    # Наименование товаров в списке
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Кнопка сортировки по цене
    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Цена товаров в результате поиска
    products_prices = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')

    # Кнопка вэб-элемента "каталог товаров"
    find_run_button = WebElement(xpath='//button[@type="button"]')

    # Ссылка на вэб-элемент "баллы"
    find_run_btn_a = WebElement(xpath='//a[button/span/div[2]]')

    # Ссылка на вэб-элемент "заказы"
    find_run_btn_b = WebElement(xpath='//a[contains(span/div[2]) and text()="заказы")]')

    # Ссылка на вэб-элемент "избранное"
    find_run_btn_c = WebElement(xpath='//a[contains(span/div[2]) and text()="избранное")]')

    # Ссылка на вэб-элемент "корзина"
    find_run_btn_d = WebElement(xpath='//a[contains(span/div[2]) and text()="корзина")]')

    # Кнопка вэб-элемента "Москва"
    find_run_btn_e = WebElement(xpath='//button[@type="Москва"]')

    # Ссылка на вэб-элемент "черная Пятница"
    find_run_btn_f = WebElement(xpath='//a[contains(@href, "/special/black-friday")]')

    # Ссылка на вэб-элемент "экспресс"
    find_run_btn_g = WebElement(xpath='//a[contains(@href, "/catalog--express/23272130")]')

    # Ссылка на вэб-элемент "одежда"
    find_run_btn_h = WebElement(xpath='//a[contains(@href, "/catalog--odezda-obuv-i-aksessuary/54432")]')

    # Ссылка на вэб-элемент "электроника"
    find_run_btn_i = WebElement(xpath='//a[contains(@href, "/catalog--elektronika/54440")]')

    # Ссылка на вэб-элемент "бытовая техника"
    find_run_btn_j = WebElement(xpath='//a[contains(@href, "/catalog--bytovaia-tekhnika/54419")]')

    # Ссылка на вэб-элемент "дом"
    find_run_btn_k = WebElement(xpath='//a[contains(@href, "/catalog--tovary-dlia-doma/54422")]')

    # Ссылка на вэб-элемент "детям"
    find_run_btn_l = WebElement(xpath='//a[contains(@href, "/catalog--detskie-tovary/54421")]')

    # Ссылка на вэб-элемент "трансляции"
    find_run_btn_m = WebElement(xpath='//a[contains(@href, "/live")]')

    # Ссылка на вэб-элемент "продавайте на маркете"
    find_run_btn_n = WebElement(css_selector='а._3Lwc_')