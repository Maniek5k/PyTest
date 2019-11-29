from selenium.webdriver.common.by import By

from conftest import BaseTest
from conftest import services
from pages.page_register import PageReg

class TestRegister(BaseTest):
    def test_register(self):
        self.driver.get(PageReg.register_url)

        services.assert_and_click(self, By.CSS_SELECTOR, PageReg.register_btn)

        services.send_keys_by_xpath(self, PageReg.register_fname, PageReg.register_data_fname)

        services.send_keys_by_xpath(self, PageReg.register_lname, PageReg.register_data_lname)

        services.send_keys_by_xpath(self, PageReg.register_mail, PageReg.register_data_mail)

        services.send_keys_by_xpath(self, PageReg.register_phone, PageReg.register_data_phone)

        services.send_keys_by_xpath(self, PageReg.register_pwd, PageReg.register_data_pwd)

        services.send_keys_by_xpath(self, PageReg.register_pwd_conf, PageReg.register_data_pwd)

        services.assert_and_click(self, By.NAME, PageReg.register_checkbox)

        services.assert_and_click(self, By.CSS_SELECTOR, PageReg.register_submit)

        assert services.get_text_by_xpath(self, PageReg.register_success_h1) == "Account"

        services.assert_and_click(self, By.CSS_SELECTOR, PageReg.register_success_continue)

        services.assert_and_click(self, By.LINK_TEXT, PageReg.register_logout)