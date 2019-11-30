import time

from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_login import login


class TestPwdChange(Base):
    def test_pwd_change(self):
        self.driver.get(login.login_url)

        services.send_keys_by_xpath(self, login.login_mail_input, login.pwd_change_mail)

        login.check_login(self)

        services.assert_and_click(self, By.LINK_TEXT, login.login_pwd_change)

        services.send_keys_by_xpath(self, login.login_pwd_input, login.pwd_change_changed_pass)

        services.send_keys_by_xpath(self, login.pwd_change_input_confirm, login.pwd_change_changed_pass)

        services.assert_and_click(self, By.XPATH, login.pwd_change_submit)

        login.check_logout(self)

        self.driver.get(login.login_url)

        services.send_keys_by_xpath(self, login.login_mail_input, login.pwd_change_mail)

        services.send_keys_by_xpath(self, login.login_pwd_input, login.pwd_change_changed_pass)

        services.assert_and_click(self, By.CSS_SELECTOR, login.login_submit)

        services.assert_and_click(self, By.LINK_TEXT, login.login_pwd_change)

        services.send_keys_by_xpath(self, login.login_pwd_input, login.pwd_change_default_pass)

        services.send_keys_by_xpath(self, login.pwd_change_input_confirm, login.pwd_change_default_pass)

        services.assert_and_click(self, By.XPATH, login.pwd_change_submit)

        services.assert_text(self, By.CSS_SELECTOR, login.login_alert, login.pwd_change_success)

        login.check_logout(self)