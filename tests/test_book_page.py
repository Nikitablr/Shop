from pages.base_page import BasePage
from pages.register_login_page import LoginPage
from pages.book_page import BookPage

def test_book_hotel(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = LoginPage(browser)
    page.open_login_page()
    page.login_user()
    page = BookPage(browser)
    page.open_book_accommodation()
    page.open_hotel1_page()
    page.book_hotel()
    page.open_cart_page()
    page.check_add()

def test_delete_book(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = LoginPage(browser)
    page.open_login_page()
    page.login_user()
    page = BookPage(browser)
    page.delete_book()



