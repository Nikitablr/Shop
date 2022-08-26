from pages.profiles_page import ProfilePage
from pages.base_page import BasePage
from pages.register_login_page import LoginPage


def test_change_profile_name(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = LoginPage(browser)
    page.open_login_page()
    page.login_user()
    page = ProfilePage(browser)
    page.open_profile_page()
    page.enter_new_name()
    page.click_save_button()
    page.check_change_name()

def test_change_invalid_age(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = LoginPage(browser)
    page.open_login_page()
    page.login_user()
    page = ProfilePage(browser)
    page.open_profile_page()
    page.enter_invalid_age()
    page.click_save_button()
    page.error_age_message()


