from pages.profiles_page import ProfilePage
from pages.register_login_page import LoginPage


def test_change_profile_name(browser):
    page = LoginPage(browser)
    page.go_to_site()
    page.open_login_page()
    page.login_user()
    page = ProfilePage(browser)
    page.open_profile_page()
    page.enter_new_name()
    page.click_save_button()
    page.check_change_name()

def test_change_invalid_age(browser):
    page = LoginPage(browser)
    page.go_to_site()
    page.open_login_page()
    page.login_user()
    page = ProfilePage(browser)
    page.open_profile_page()
    page.enter_invalid_age()
    page.click_save_button()
    page.error_age_message()


