from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_login import login
from pages.page_account import account


class TestNewsletter(Base):
    def test_newsletter(self):
        self.driver.get(login.login_url)

        services.send_keys_by_xpath(self, login.login_mail_input, account.account_mail_newsletter)

        login.check_login(self)

        services.assert_and_click(self, By.LINK_TEXT, account.account_newsletter)

        services.assert_and_click(self, By.XPATH, account.account_newsletter_1)

        services.assert_and_click(self, By.CSS_SELECTOR, account.account_submit)

        services.assert_and_click(self, By.LINK_TEXT, account.account_newsletter)

        services.assert_and_click(self, By.XPATH, account.account_newsletter_0)

        services.assert_and_click(self, By.CSS_SELECTOR, account.account_submit)

        login.check_logout(self)