# Test for returning ordered product

from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_checkout import checkout
from pages.page_login import login
from pages.page_basket import basket


class TestReturn(Base):
    def test_return(self):
        self.driver.get(login.login_url)

        services.send_keys_by_xpath(self, login.login_mail_input, checkout.checkout_return_email)

        login.check_login(self)

        services.assert_and_click(self, By.LINK_TEXT, basket.reorder_history)

        services.assert_and_click(self, By.CSS_SELECTOR, basket.reorder_view)

        services.assert_and_click(self, By.CSS_SELECTOR, checkout.return_button)

        services.assert_and_click(self, By.CSS_SELECTOR, checkout.return_submit)

        services.assert_text(self, By.CSS_SELECTOR, checkout.return_necessary_option, checkout.return_option_text)

        services.assert_and_click(self, By.NAME, checkout.return_radio)

        services.assert_and_click(self, By.CSS_SELECTOR, checkout.return_submit)

        services.assert_text(self, By.XPATH, checkout.return_success, checkout.return_success_text)

        login.check_logout(self)
