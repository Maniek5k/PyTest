from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_login import login
from pages.page_account import account


class TestAddAddress(Base):
    def test_login_success(self):
        self.driver.get(login.login_url)

        services.send_keys_by_xpath(
            self, login.login_mail_input, account.account_mail_edit
        )

        login.check_login(self)

        services.assert_and_click(self, By.LINK_TEXT, account.account_address_book)

        services.assert_and_click(self, By.CSS_SELECTOR, account.account_address_edit)

        services.clear_element_by_xpath(self, account.account_postcode)

        services.send_keys_by_xpath(
            self, account.account_postcode, account.account_data_random
        )

        services.assert_and_click(self, By.CSS_SELECTOR, account.account_submit)

        services.is_element_visible(self, By.CSS_SELECTOR, account.account_success)

        services.assert_text(
            self,
            By.CSS_SELECTOR,
            account.account_success,
            account.account_edit_address_text,
        )

        login.check_logout(self)
