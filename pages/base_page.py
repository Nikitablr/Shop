from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(10)

    def go_to_site(self):
        url = 'https://cypress-tourism-app.herokuapp.com/'
        self.browser.get(url)

    def scroll_to_element(self, *how):
        element = self.browser.find_element(*how)
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()

    def is_presented(self, how, what):
        element = self.browser.find_element(how, what)
        return element is not None

    def is_open(self, how, what):
        element = self.browser.find_element(how, what)
        return element is not None


