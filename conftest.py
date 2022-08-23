import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    yield driver
    time.sleep(20)
    driver.quit()
