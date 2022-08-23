from pages.profiles_page import ProfilePage
from test_signin_signup_page import*


def test_change_profile_name(browser):
    test_signin_user(browser)
    page = ProfilePage(browser)
    page.open_profile_page()
    page.enter_new_name()
    page.click_save_button()
    page.check_change_name()

def test_change_invalid_age(browser):
    test_signin_user(browser)
    page = ProfilePage(browser)
    page.open_profile_page()
    page.enter_invalid_age()
    page.click_save_button()
    page.error_age_message()

