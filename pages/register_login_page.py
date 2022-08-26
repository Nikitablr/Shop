from pages.base_page import BasePage
from .locator import LoginLocator
from .locator import SignupLocator
from models.register_faker import RegisterData


class LoginPage(BasePage):

    def open_login_page(self):
        self.browser.find_element(*LoginLocator.SIGN_IN_BUTTON).click()

    def open_signup_page(self):
        self.browser.find_element(*SignupLocator.SIGN_UP_BUTTON).click()

    def enter_first_name(self, name):
        new_user = self.browser.find_element(*SignupLocator.NEW_USER_NAME)
        new_user.send_keys(name)

    def enter_last_name(self, first_name):
        name = self.browser.find_element(*SignupLocator.NEW_USER_FIRST_NAME)
        name.send_keys(first_name)

    def enter_password(self, password):
        passwo = self.browser.find_element(*SignupLocator.PASSWORD)
        passwo.send_keys(password)

    def enter_confirm_password(self, conf_password):
        confirm_password = self.browser.find_element(*SignupLocator.CONFIRM_PASSWORD)
        confirm_password.send_keys(conf_password)

    def enter_email_address(self, email):
        email_address = self.browser.find_element(*SignupLocator.EMAIL_ADDRESS)
        email_address.send_keys(email)

    def click_register_button(self):
        register_button = self.browser.find_element(*SignupLocator.REGISTER_BUTTON)
        register_button.click()

    def click_signin_button(self):
        register_button = self.browser.find_element(*LoginLocator.LOGIN_BUTTON)
        register_button.click()

    def enter_login_password(self, password):
        passwo = self.browser.find_element(*LoginLocator.PASSWORD_FIELD)
        passwo.send_keys(password)

    def click_logout_button(self):
        logout = self.browser.find_element(*LoginLocator.LOGOUT_BUTTON)
        logout.click()

    '''Заполняем форму регистрации валидными данными'''
    def fill_fields_valid(self):
        data = RegisterData.random()
        self.enter_first_name(data.first_name)
        self.enter_last_name(data.last_name)
        self.enter_password(data.password)
        self.enter_confirm_password(data.password_2)
        self.enter_email_address(data.email)
        self.scroll_to_element(*SignupLocator.REGISTER_BUTTON)
        self.click_register_button()
        assert self.is_open(*SignupLocator.OPEN_AFTER_SIGNUP)

    '''Вводим разные пароли'''
    def enter_did_not_match_password(self):
        data = RegisterData.random()
        self.enter_first_name(data.first_name)
        self.enter_last_name(data.last_name)
        self.enter_password(data.password)
        data = RegisterData.random_did_not_match_pass()
        self.enter_confirm_password(data.password_2)
        self.click_register_button()
        assert self.is_presented(*SignupLocator.MESSAGE_DID_NOT_MATCH_PASSWORD)

    '''Авторизация ранее зарегистрированного пользователя'''
    def enter_registered_user_name(self):
        self.enter_first_name('Nik')
        self.enter_password('Nik123456')
        self.enter_confirm_password('Nik123456')
        self.click_register_button()
        assert self.is_presented(*SignupLocator.MESSAGE_USER_ALREADY_EXIST)

    '''Авторизация ранее зарегистрированного пользователя'''
    def login_user(self):
        self.enter_first_name('Nik')
        self.enter_login_password('Nik123456')
        self.click_signin_button()
        assert self.is_presented(*LoginLocator.DROPDOWN_IF_USER_LOGIN)

    '''Вводим не верное username при авторизации'''
    def login_user_with_invalid_username(self):
        self.enter_first_name('n')
        self.enter_login_password('Nik123456')
        self.click_signin_button()
        assert self.is_presented(*LoginLocator.ERROR_MESSAGE_IF_INVALID_NAME)

    def logout_user(self):
        self.enter_first_name('nik')
        self.enter_login_password('Nik123456')
        self.click_signin_button()
        self.click_logout_button()
        assert self.is_open(*LoginLocator.SIGNIN_BUTTON_APPEAR)








