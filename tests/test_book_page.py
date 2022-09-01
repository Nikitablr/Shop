from pages.register_login_page import LoginPage
from pages.book_page import BookPage


def test_booking_hotel(browser):
    page = LoginPage(browser)
    page.go_to_site()
    page.open_login_page()
    page.login_user()
    page = BookPage(browser)
    page.open_book_accommodation()
    page.open_hotel1_page()
    page.book_hotel()
    page.open_cart_page()
    page.check_add()
    page.check_name()
    page.check_cost()

def test_delete_booking(browser):
    test_booking_hotel(browser)
    page = BookPage(browser)
    page.delete_book()





