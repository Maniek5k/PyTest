# File with all helper functions, used to execute operations on website.

import random

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def driver_init(request):
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('no-cache')
    options.add_argument('no-sandbox')
    options.add_argument('disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    driver.get("http://tutorialsninja.com/demo/")
    driver.implicitly_wait(10)
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

    def wait_for_title(self, title, timeout=20):
        LOGGER.info("Waiting for title to contain %s" % title)
        WebDriverWait(self.driver, timeout).until(EC.title_contains(title))

    def is_element_visible(self, how, locator, timeout=20):
        LOGGER.info("Waiting until element %s is visible" % locator)
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, locator)))
        except NoSuchElementException:
            LOGGER.error("Element %s is not visible" % locator)
            self.driver.close()
            return False

    def send_keys_by_xpath(self, locator, keys):
        LOGGER.info("Filling input %s with %s" % (locator, keys))
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

    def assert_and_click(self, how, locator, timeout=20):
        LOGGER.info("Waiting for element %s" % locator)
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((how, locator)))
        LOGGER.info("Clicking element %s" % locator)
        ele = self.driver.find_element(how, locator)
        ele.click()

    def get_text(self, how, locator):
        LOGGER.info("Getting text from element %s" % locator)
        return self.driver.find_element(how, locator).text

    def assert_text(self, how, locator, text_, timeout=20):
        LOGGER.info("Getting text from element %s and comparing with target text" % locator)
        assert WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((how, locator), text_))

