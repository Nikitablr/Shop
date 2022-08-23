from pages.base_page import BasePage
from .locator import BookLocator

class BookPage(BasePage):

    def open_book_accommodation(self):
        self.browser.find_element(*BookLocator.BOOK_ACCOMODATION_BUTTON).click()

    def open_hotel1_page(self):
        self.browser.find_element(*BookLocator.MORE_BUTTON).click()

    def book_hotel(self):
        self.browser.find_element(*BookLocator.BOOK_BUTTON).click()

    def open_cart_page(self):
        self.browser.find_element(*BookLocator.DROPDOWN_BUTTON).click()
        self.browser.find_element(*BookLocator.BASKET_BUTTON).click()

    def check_add(self):
        assert self.is_presented(*BookLocator.CHECK_ADD)

    def delete_book(self):
        self.browser.find_element(*BookLocator.DELETE_BUTTON).click()
        assert self.is_presented(*BookLocator.EMPTY_CART)




