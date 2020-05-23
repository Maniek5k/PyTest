# Test for checking checkout process with verification for error & success messages

import pytest
from selenium.webdriver.common.by import By
from conftest import Base, services
from pages.page_basket import basket
from pages.page_checkout import checkout
from pages.page_login import login


class TestCheckout(Base):
    @pytest.mark.skip(reason="Checkout shouldn't be tested in a suite")
    def test_checkout(self):
        self.driver.get(login.login_url)

        services.send_keys_by_xpath(
            self, login.login_mail_input, checkout.checkout_mail
        )

        login.check_login(self)

        self.driver.get(basket.basket_pp)

        services.assert_and_click(self, By.XPATH, basket.basket_add)

        services.assert_and_click(self, By.XPATH, basket.basket_cart)

        services.assert_and_click(self, By.LINK_TEXT, checkout.checkout_btn)

        services.assert_and_click(self, By.XPATH, checkout.checkout_payment)

        services.assert_and_click(self, By.XPATH, checkout.checkout_shipping)

        services.assert_and_click(self, By.XPATH, checkout.checkout_shipping_method)

        services.assert_and_click(self, By.XPATH, checkout.checkout_payment_method)

        services.assert_text(
            self,
            By.CSS_SELECTOR,
            checkout.checkout_alert_checkbox,
            checkout.checkout_alert_msg,
        )

        services.assert_and_click(self, By.NAME, checkout.checkout_checkbox)

        services.assert_and_click(self, By.XPATH, checkout.checkout_payment_method)

        services.assert_and_click(self, By.XPATH, checkout.checkout_confirm)

        services.wait_for_title(self, checkout.checkout_placed_title)
        services.assert_text(
            self,
            By.XPATH,
            checkout.checkout_order_placed,
            checkout.checkout_order_placed_msg,
        )

        self.driver.get(login.login_url)

        login.check_logout(self)
