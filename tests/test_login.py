from selenium.webdriver.common.by import By
from selenium import webdriver

from conftest import BaseTest
from conftest import services
from pages.page_login import PageLogin


class TestLogin(BaseTest):
    def test_login(self):
        self.driver.get(PageLogin.login_url)

        services.send_keys_by_xpath(self, PageLogin.login_mail_input, PageLogin.login_mail)

        services.send_keys_by_xpath(self, PageLogin.login_pwd_input, PageLogin.login_pwd)

        services.assert_and_click(self, By.CSS_SELECTOR, PageLogin.login_submit)

        assert services.get_text_by_xpath(self, PageLogin.login_my_acc) == "My Account"

        services.assert_and_click(self, By.LINK_TEXT, PageLogin.login_logout)