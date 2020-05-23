from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_login import login


class TestLoginFailed(Base):
    def test_login_failed(self):
        self.driver.get(login.login_url)

        services.send_keys_by_xpath(self, login.login_mail_input, login.login_fail_mail)

        services.send_keys_by_xpath(self, login.login_pwd_input, login.login_fail_pwd)

        services.assert_and_click(self, By.CSS_SELECTOR, login.login_submit)

        services.assert_text(
            self, By.CSS_SELECTOR, login.login_alert, login.login_fail_msg
        )
