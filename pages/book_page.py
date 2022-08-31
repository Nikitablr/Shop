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
        assert self.is_presented(*BookLocator.CHECK_ADD), "Hotel don't added"

    def check_name(self):
        self.browser.switch_to.new_window('window')
        booking_url = 'https://cypress-tourism-app.herokuapp.com/list_of_accommodations/'
        self.browser.get(booking_url)
        name_hotel = self.browser.find_element(*BookLocator.NAME_ON_BOOK_PAGE).text
        self.browser.switch_to.window(self.browser.window_handles[0])
        name_hotel_in_cart = self.browser.find_element(*BookLocator.NAME_ON_CART_PAGE).text
        assert name_hotel in name_hotel_in_cart, "Names don't match"

    def delete_book(self):
        button = self.browser.find_element(*BookLocator.DELETE_BUTTON)
        button.click()
        assert self.is_presented(*BookLocator.EMPTY_CART), 'Cart not cleared'




