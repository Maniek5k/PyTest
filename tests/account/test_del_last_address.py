from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_login import login
from pages.page_account import account


class TestLastAddress(Base):
    def test_last_address(self):
        self.driver.get(login.login_url)

        services.send_keys_by_xpath(self, login.login_mail_input, account.account_mail_failed)

        login.check_login(self)

        services.assert_and_click(self, By.LINK_TEXT, account.account_address_book)

        services.assert_and_click(self, By.CSS_SELECTOR, account.account_delete)

        services.assert_text(self, By.CSS_SELECTOR, account.account_failed, account.account_last_address_text)

        login.check_logout(self)