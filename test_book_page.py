from pages.book_page import BookPage
from test_signin_signup_page import*

def test_book_hotel(browser):
    test_signin_user(browser)
    page = BookPage(browser)
    page.open_book_accommodation()
    page.open_hotel1_page()
    page.book_hotel()
    page.open_cart_page()
    page.check_add()

def test_delete_book(browser):
    test_book_hotel(browser)
    page = BookPage(browser)
    page.delete_book()



