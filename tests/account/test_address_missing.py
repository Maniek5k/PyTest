from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_login import login
from pages.page_account import account


class TestAddressMissingFields(Base):
    def test_address_missing_fields(self):
        self.driver.get(login.login_url)

        services.send_keys_by_xpath(self, login.login_mail_input, account.account_mail_missing)

        login.check_login(self)

        services.assert_and_click(self, By.LINK_TEXT, account.account_address_book)

        services.assert_and_click(self, By.LINK_TEXT, account.account_add_address)

        services.assert_and_click(self, By.CSS_SELECTOR, account.account_submit)

        services.assert_text(self, By.CSS_SELECTOR, account.account_missing, account.account_missing_text)

        login.check_logout(self)