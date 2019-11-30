from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_login import login
from pages.page_account import account


class TestAddAddress(Base):
    def test_add_address(self):
        self.driver.get(login.login_url)

        services.send_keys_by_xpath(self, login.login_mail_input, account.account_mail)

        login.check_login(self)

        services.assert_and_click(self, By.LINK_TEXT, account.account_address_book)

        services.assert_and_click(self, By.LINK_TEXT, account.account_add_address)

        services.send_keys_by_xpath(self, account.account_fname, account.account_data)

        services.send_keys_by_xpath(self, account.account_lname, account.account_data)

        services.send_keys_by_xpath(self, account.account_company, account.account_data)

        services.send_keys_by_xpath(self, account.account_address1, account.account_data)

        services.send_keys_by_xpath(self, account.account_address2, account.account_data)

        services.send_keys_by_xpath(self, account.account_city, account.account_data)

        services.send_keys_by_xpath(self, account.account_postcode, account.account_data_postcode)

        services.assert_and_click(self, By.XPATH, account.account_region_select)

        services.assert_and_click(self, By.CSS_SELECTOR, account.account_submit)

        services.assert_text(self, By.CSS_SELECTOR, account.account_success, account.account_added_text)

        services.assert_and_click(self, By.CSS_SELECTOR, account.account_delete)

        services.assert_text(self, By.CSS_SELECTOR, account.account_success, account.account_deleted_text)

        login.check_logout(self)