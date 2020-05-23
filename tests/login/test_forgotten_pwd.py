from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_login import login


class TestForgottenPwd(Base):
    def test_forgotten_pwd(self):
        self.driver.get(login.login_url)

        services.assert_and_click(self, By.LINK_TEXT, login.login_forgotten_pwd)

        services.send_keys_by_xpath(self, login.login_mail_input, login.login_fail_mail)

        services.assert_and_click(self, By.CSS_SELECTOR, login.login_submit)

        services.assert_text(
            self, By.CSS_SELECTOR, login.login_alert, login.login_forgotten_msg_alert
        )

        services.clear_element_by_xpath(self, login.login_mail_input)

        services.send_keys_by_xpath(self, login.login_mail_input, login.login_mail)

        services.assert_and_click(self, By.CSS_SELECTOR, login.login_submit)

        services.assert_text(
            self, By.CSS_SELECTOR, login.login_alert, login.login_forgotten_msg_success
        )
