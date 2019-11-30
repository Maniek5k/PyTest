import random
from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import logging

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def driver_init(request):
    from selenium import webdriver
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.get("http://tutorialsninja.com/demo/")
    yield
    driver.close()


@pytest.mark.usefixtures("driver_init")
class Base:
    pass


class services:

    def __init__(self):
        LOGGER.info("Opening Chrome")
        self.driver = webdriver.Chrome()

    def create_random_prefix(self):
        self.prefix_created = str(random.randint(0, 99999))
        return self.prefix_created

    def wait_for_element(self, how, locator, timeout=20):
        LOGGER.info("Waiting for element %s" % locator)
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, locator)))

    def is_element_visible(self, how, locator):
        LOGGER.info("Checking if element %s is visible" % locator)
        try:
            LOGGER.info("Waiting until element %s is visible and checking assertion" % locator)
            assert self.driver.find_element(how, locator)
        except NoSuchElementException:
            LOGGER.error("Element %s is not visible" % locator)
            self.driver.close()
            return False

    def send_keys_by_xpath(self, locator, keys):
        LOGGER.info("Filling input with %s" % keys)
        element = self.driver.find_element_by_xpath(locator)
        element.send_keys(keys)
        assert True

    def submit_form_by_xpath(self, locator, keys):
        LOGGER.info("Submitting form %s" % locator)
        element = self.driver.find_element_by_xpath(locator)
        element.send_keys(keys)
        element.submit()

    def clear_element_by_xpath(self, locator):
        LOGGER.info("Clearing element %s" % locator)
        element = self.driver.find_element_by_xpath(locator)
        element.clear()

    def assert_and_click(self, how, locator):
        LOGGER.info("Clicking element %s" % locator)
        ele = self.driver.find_element(how, locator)
        ele.click()

    def get_text(self, how, locator):
        LOGGER.info("Getting text from element %s" % locator)
        return self.driver.find_element(how, locator).text

    def assert_text(self, how, locator, target):
        LOGGER.info("Getting text from element %s and comparing with target text" % locator)
        assert services.get_text(self, how, locator) == target

    def assert_element_present(self, how, locator):
        LOGGER.info("Checking is element %s is present" % locator)
        assert services.is_element_visible(self, how, locator)

    def wait_for_element_visible(self, how, locator, timeout=20):
        LOGGER.info("Waiting until element %s is visible" % locator)
        WebDriverWait(self.driver, timeout).until(services.is_element_visible(self, how, locator))