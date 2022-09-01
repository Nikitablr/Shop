from selenium.webdriver.common.by import By

class SignupLocator:
    SIGN_UP_BUTTON = (By.XPATH, '//button[@class = "btn btn-round form-control"]')
    NEW_USER_NAME = (By.NAME, 'username')
    NEW_USER_FIRST_NAME = (By.NAME, 'first_name')
    PASSWORD = (By.NAME, 'password1')
    CONFIRM_PASSWORD = (By.NAME, 'password2')
    EMAIL_ADDRESS = (By.ID, 'id_email')
    REGISTER_BUTTON = (By.XPATH, '/html/body/div/div[2]/div/form/input[2]')
    MESSAGE_DID_NOT_MATCH_PASSWORD = (By.XPATH, '/html/body/div/div[2]/div/form/ul/li')
    OPEN_AFTER_SIGNUP = (By.XPATH, '/html/body/div/div[2]/div/div')
    MESSAGE_USER_ALREADY_EXIST = (By.XPATH, '/html/body/div/div[2]/div/form/ul/li')

class LoginLocator:
    SIGN_IN_BUTTON = (By.XPATH, '//*[@id="navbarTogglerDemo01"]/ul/li[3]/a')
    USER_NAME_FIELD = (By.NAME, 'username')
    PASSWORD_FIELD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '/html/body/div/div[2]/div/form/input[2]')
    DROPDOWN_IF_USER_LOGIN = (By.XPATH, '//*[@id="navbarTogglerDemo01"]/ul/li[2]/a')
    ERROR_MESSAGE_IF_INVALID_NAME = (By.XPATH, '/html/body/div/div[2]/div/form/ul/li')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="navbarTogglerDemo01"]/ul/li[3]/a')
    SIGNIN_BUTTON_APPEAR = (By.XPATH, '//*[@id="navbarTogglerDemo01"]/ul/li[3]/a')

class BookLocator:
    BOOK_ACCOMODATION_BUTTON = (By.XPATH, '//*[@id="navbarTogglerDemo01"]/ul/li[1]/a')
    MORE_BUTTON = (By.XPATH, '/html/body/div/div[2]/div/div[1]/div/a')
    BOOK_BUTTON = (By.XPATH, '/html/body/div/div[2]/div[1]/div/div/div/button/a')
    COST_ON_BOOK_PAGE = (By.XPATH, '/html/body/div/div[2]/div/div[1]/div/p[2]')
    COST_ON_CART_PAGE = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div[1]/span[3]')
    NAME_ON_BOOK_PAGE = (By.CLASS_NAME, 'card-title')
    NAME_ON_CART_PAGE = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div[1]/span[2]')
    DROPDOWN_BUTTON = (By.XPATH, '//*[@id="navbarTogglerDemo01"]/ul/li[2]/a')
    BASKET_BUTTON = (By.XPATH, '//*[@id="navbarTogglerDemo01"]/ul/li[2]/div/a[2]')
    CHECK_ADD = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div[1]')
    EMPTY_CART = (By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div[1]/h6')
    DELETE_BUTTON = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div[2]/button/a')


class ProfileLocator:
    PROFILE_BUTTON = (By.XPATH, '//*[@id="navbarTogglerDemo01"]/ul/li[2]/div/a[1]')
    USERNAME_FIELD = (By.ID, 'id_username')
    SAVE_BUTTON = (By.XPATH, '/html/body/div/div[2]/div[2]/form/input[2]')
    CHECK_CHANGED_NAME = (By.XPATH, '//*[@id="navbarTogglerDemo01"]/ul/li[2]/a')
    AGE_ERROR_MESSAGE = (By.XPATH, '/html/body/div/div[2]/div[2]/form/ul/li')
    AGE_FIELD = (By.ID, 'id_age')