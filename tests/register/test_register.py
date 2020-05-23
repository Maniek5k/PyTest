# Test for general registration checking

from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_login import login
from pages.page_register import register


class TestRegister(Base):
    def test_register(self):
        self.driver.get(register.register_url)

        services.assert_and_click(self, By.CSS_SELECTOR, register.register_btn)

        services.send_keys_by_xpath(
            self, register.register_fname, register.register_data_fname
        )

        services.send_keys_by_xpath(
            self, register.register_lname, register.register_data_lname
        )

        services.send_keys_by_xpath(
            self, register.register_mail, register.register_data_mail
        )

        services.send_keys_by_xpath(
            self, register.register_phone, register.register_data_phone
        )

        services.send_keys_by_xpath(
            self, register.register_pwd, register.register_data_pwd
        )

        services.send_keys_by_xpath(
            self, register.register_pwd_conf, register.register_data_pwd
        )

        services.assert_and_click(self, By.NAME, register.register_checkbox)

        services.assert_and_click(self, By.CSS_SELECTOR, register.register_submit)

        services.assert_text(self, By.XPATH, register.register_success_h1, "Account")

        services.assert_and_click(
            self, By.CSS_SELECTOR, register.register_success_continue
        )

        login.check_logout(self)
