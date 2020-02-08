# Test for checking checkout process with verification for error & success messages

import time

from selenium.webdriver.common.by import By

from conftest import Base, services
from pages.page_basket import basket
from pages.page_checkout import checkout
from pages.page_login import login


class TestCheckout(Base):
    def test_checkout(self):
        self.driver.get(login.login_url)

        services.send_keys_by_xpath(self, login.login_mail_input, checkout.checkout_mail)

        login.check_login(self)

        self.driver.get(basket.basket_pp)

        services.assert_and_click(self, By.XPATH, basket.basket_add)

        services.assert_and_click(self, By.XPATH, basket.basket_cart)

        services.assert_and_click(self, By.LINK_TEXT, checkout.checkout_btn)
        time.sleep(1)
        services.assert_and_click(self, By.XPATH, checkout.checkout_payment)
        time.sleep(1)
        services.assert_and_click(self, By.XPATH, checkout.checkout_shipping)
        time.sleep(1)
        services.assert_and_click(self, By.XPATH, checkout.checkout_shipping_method)
        time.sleep(1)
        services.assert_and_click(self, By.XPATH, checkout.checkout_payment_method)
        time.sleep(1)
        services.assert_text(self, By.CSS_SELECTOR, checkout.checkout_alert_checkbox, checkout.checkout_alert_msg)
        time.sleep(1)
        services.assert_and_click(self, By.NAME, checkout.checkout_checkbox)
        time.sleep(1)
        services.assert_and_click(self, By.XPATH, checkout.checkout_payment_method)
        time.sleep(1)
        services.assert_and_click(self, By.XPATH, checkout.checkout_confirm)
        time.sleep(1)
        services.assert_text(self, By.XPATH, checkout.checkout_order_placed, checkout.checkout_order_placed_msg)

        self.driver.get(login.login_url)

        login.check_logout(self)
