from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_login import login
from pages.page_account import account


class TestAffiliate(Base):
    def test_affiliate(self):
        self.driver.get(login.login_url)

        services.send_keys_by_xpath(
            self, login.login_mail_input, account.account_mail_affiliate
        )

        login.check_login(self)

        services.assert_and_click(self, By.LINK_TEXT, account.account_affiliate)

        services.send_keys_by_xpath(
            self, account.account_affiliate_tax, account.account_data_random
        )

        services.assert_and_click(self, By.CSS_SELECTOR, account.account_submit)

        services.assert_text(
            self, By.CSS_SELECTOR, account.account_success, account.account_updated
        )

        login.check_logout(self)
