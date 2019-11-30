from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_login import login


class TestLoginSuccess(Base):
    def test_login_success(self):
        self.driver.get(login.login_url)

        services.send_keys_by_xpath(self, login.login_mail_input, login.login_mail)

        services.send_keys_by_xpath(self, login.login_pwd_input, login.login_pwd)

        services.assert_and_click(self, By.CSS_SELECTOR, login.login_submit)

        services.assert_text(self, By.XPATH, login.login_my_acc, login.login_success)

        services.assert_and_click(self, By.LINK_TEXT, login.login_logout)

        services.assert_text(self, By.XPATH, login.logout_success, login.logout_success_text)