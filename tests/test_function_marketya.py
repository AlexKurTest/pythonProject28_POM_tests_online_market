# Командная строка для запуска автоматических тестов через терминал:
# python -m pytest -v --driver Chrome --driver-path C:\DriversWeb\chromedriver.exe tests\test_function_marketya.py
import pytest
from pages.marketya import MainPage

def test_open_catalog(web_browser):
    page = MainPage(web_browser)
    page.find_run_button = 'каталог товаров'
    page.find_run_button.click()
    assert page.open_new_page == page.open_catalog

def test_open_scores(web_browser):
    page = MainPage(web_browser)
    page.find = 'баллы'
    page.find_run_btn.click()
    assert page.open_new_page == page.open_scores

def test_open_orders(web_browser):
    page = MainPage(web_browser)
    page.find = 'заказы'
    page.find_run_btn.click()
    assert page.open_new_page == page.open_orders

def test_open_favorites(web_browser):
    page = MainPage(web_browser)
    page.find = 'избранное'
    page.find_run_btn.click()
    assert page.open_new_page == page.open_favorites

def test_open_bascet(web_browser):
    page = MainPage(web_browser)
    page.find = 'корзина'
    page.find_run_btn.click()
    assert page.open_new_page == page.open_basket

def test_open_Moscow(web_browser):
    page = MainPage(web_browser)
    page.find = 'Mocква'
    page.find_run_btn.click()
    assert page.open_new_page == page.open_map

def test_open_black_friday(web_browser):
    page = MainPage(web_browser)
    page.find = 'черная пятница'
    page.find_run_btn_f.click()
    assert page.open_new_page == page.open_black_friday

def test_open_express(web_browser):
    page = MainPage(web_browser)
    page.find = 'экспресс'
    page.find_run_btn_g.click()
    assert page.open_new_page == page.open_express_page

def test_open_odezda(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'одежда'
    page.find_run_btn_h.click()
    assert page.open_new_page == page.open_odezda

def test_open_electronics(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'электроника'
    page.find_run_btn_i.click()
    assert page.open_new_page == page.open_electronics

def test_open_bittehnika(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'бытовая техника'
    page.find_run_btn_j.click()
    assert page.open_new_page == page.open_bittehnika

def test_open_tovary_dlia_doma(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'товары для дома'
    page.find_run_btn_k.click()
    assert page.open_new_page == page.open_bittehnika

def test_open_children(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'дeтям'
    page.find_run_btn_l.click()
    assert page.open_new_page == page.open_children

def test_open_broadcasts(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'трансляции'
    page.find_run_btn_m.click()
    assert page.open_new_page == page.open_broadcasts-page

def test_open_sell_on_the_market(web_browser):
    page = MainPage(web_browser)
    page.find.element = 'продавайте на маркете'
    page.find_run_btn_n.click()
    assert page.open_new_page == page.open_sell_on_the_market

def test_check_main_search_rus(web_browser):
    """ Make sure main search works fine. """
    page = MainPage(web_browser)
    page.search = 'cамсунг гелакси c21'
    page.search_run_button.click()
    # Verify that user can see the list of products:
    assert page.products_titles.count() >= 1
    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'samsung galaxy s21' in title.lower(), msg

def test_check_wrong_input_in_search0(web_browser):
    """ Make sure that wrong keyboard layout input works fine. """
    page = MainPage(web_browser)
    # Try to enter "смартфон" with English keyboard:
    page.search = 'cfvceyu utkfrcb c21'
    page.search_run_button.click()
    # Verify that user can see the list of products:
    assert page.products_titles.count() >= 1
    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'samsung galaxy s21' in title.lower(), msg

def test_check_main_search_eng(web_browser):
    """ Make sure main search works fine. """
    page = MainPage(web_browser)
    page.search = 'samsung galaxy s21'
    page.search_run_button.click()
    # Verify that user can see the list of products:
    assert page.products_titles.count() >= 1
    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'samsung galaxy s21' in title.lower(), msg

def test_check_wrong_input_in_search1(web_browser):
    page = MainPage(web_browser)
    page.search = 'cvfhnajy'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'смартфон' in title.lower(), msg

@pytest.mark.xfail(reason="Filter by price doesn't work")
def test_check_sort_by_price(web_browser):
    """ Make sure that sort by price works fine.
        Note: this test case will fail because there is a bug in
              sorting products by price.
    """
    page = MainPage(web_browser)
    page.search = 'тостер Philips'
    page.search_run_button.click()
    # Scroll to element before click on it to make sure
    # user will see this element in real browser
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    # Get prices of the products in Search results
    all_prices = page.products_prices.get_text()
    # Convert all prices from strings to numbers
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    # Make sure products are sorted by price correctly:
    assert all_prices == sorted(all_prices), "Сортировка по цене не работает!"

@pytest.mark.parametrize(reason="Filter by price doesn't work")
def test_check_sort_by_price(web_browser):
    page = MainPage(web_browser)
    page.search = 'Мультиварка'
    page.search_run_button.click()
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()
    all_prices = page.products_prices.get_text()
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"

def test_main_search_natural_spruse(web_browser):
    page = MainPage(web_browser)
    page.search = 'ель натуральная'
    page.search_run_button.click()
    assert page.products_titles.count() >= 1
    for title in page.products_titles.get_text():
        msg = 'Correct product in search "{}"'.format(title)
        assert 'ель природная' in title.lower(), msg
