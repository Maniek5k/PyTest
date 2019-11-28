import random
from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def driver_init(request):
    from selenium import webdriver
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.get("http://tutorialsninja.com/demo/")
    yield
    driver.close()


@pytest.mark.usefixtures("driver_init")
class BaseTest:
    pass


class services:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def create_random_prefix(self):
        self.prefix_created = str(random.randint(0, 99999))
        return self.prefix_created

    def wait_for_element(self, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))

    def is_element_visible(self, how, locator):

        try:
            self.driver.find_element(how, locator)

        except NoSuchElementException:

            self.driver.close()
            return False

    def is_element_present_xpath(self, locator):

        try:
            self.driver.find_element_by_xpath(locator)
        except NoSuchElementException:
            self.driver.close()
            return False
        return True

    def send_keys_by_xpath(self, locator, keys):

        element = self.driver.find_element_by_xpath(locator)
        element.send_keys(keys)

    def submit_form_by_xpath(self, locator, keys):

        element = self.driver.find_element_by_xpath(locator)
        element.send_keys(keys)
        element.submit()

    def clear_element_by_xpath(self, locator):
        element = self.driver.find_element_by_xpath(locator)
        element.clear()

    def assert_and_click(self, how, locator):

        ele = self.driver.find_element(how, locator)
        ele.click()

    def get_text_by_xpath(self, locator):
        return self.driver.find_element_by_xpath(locator).text

    def assert_element_present(self, how, locator):

        assert self.is_element_present(how, locator)

    def assert_element_is_not_present(self, locator):

        assert not self.is_element_present(locator)

    def wait_for_element_visible(self, locator, timeout=20):

        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))

    def wait_for_element_invisible(self, locator, timeout=20):

        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((By.XPATH, locator)))

    def assert_element_visibility(self, locator, is_visible=True):

        assert is_visible == self.is_element_visible(locator)