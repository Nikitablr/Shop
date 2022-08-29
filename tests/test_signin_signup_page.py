from pages.register_login_page import LoginPage


def test_signup_new_user(browser):
    page = LoginPage(browser)
    page.go_to_site()
    page.open_login_page()
    page.open_signup_page()
    page.fill_fields_valid()

def test_did_not_match_password(browser):
    page = LoginPage(browser)
    page.go_to_site()
    page.open_login_page()
    page.open_signup_page()
    page.enter_did_not_match_password()

def test_signup_previously_registered_user(browser):
    page = LoginPage(browser)
    page.go_to_site()
    page.open_login_page()
    page.open_signup_page()
    page.enter_registered_user_name()

def test_signin_user(browser):
    page = LoginPage(browser)
    page.go_to_site()
    page.open_login_page()
    page.login_user()

def test_signin_user_with_invalid_username(browser):
    page = LoginPage(browser)
    page.go_to_site()
    page.open_login_page()
    page.login_user_with_invalid_username()

def test_logout_user(browser):
    page = LoginPage(browser)
    page.go_to_site()
    page.open_login_page()
    page.logout_user()









