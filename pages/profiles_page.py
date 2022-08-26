from pages.base_page import BasePage
from .locator import*
from models.register_faker import RegisterData

class ProfilePage(BasePage):

    def open_profile_page(self):
        self.browser.find_element(*BookLocator.DROPDOWN_BUTTON).click()
        self.browser.find_element(*ProfileLocator.PROFILE_BUTTON).click()

    def enter_new_name(self):
        name = self.browser.find_element(*ProfileLocator.USERNAME_FIELD)
        name.clear()
        data = RegisterData.random()
        name.send_keys(self.enter_new_name(data.first_name))

    def click_save_button(self):
        self.scroll_to_element(*ProfileLocator.SAVE_BUTTON)
        self.browser.find_element(*ProfileLocator.SAVE_BUTTON).click()

    def check_change_name(self):
        new_name = 'Solo'
        name = self.browser.find_element(*ProfileLocator.CHECK_CHANGED_NAME)
        assert new_name != name

    def enter_invalid_age(self):
        name = self.browser.find_element(*ProfileLocator.AGE_FIELD)
        name.clear()
        name.send_keys("16")

    def error_age_message(self):
        assert self.browser.find_element(*ProfileLocator.AGE_ERROR_MESSAGE)







