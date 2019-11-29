import time

from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_checkout import checkout
from pages.page_login import login
from pages.page_basket import basket


class TestCheckout(Base):
    def test_checkout(self):
        self.driver.get(login.login_url)

        services.send_keys_by_xpath(self, login.login_mail_input, checkout.checkout_mail)

        services.send_keys_by_xpath(self, login.login_pwd_input, checkout.checkout_pwd)

        services.assert_and_click(self, By.CSS_SELECTOR, login.login_submit)

        services.assert_text(self, By.XPATH, login.login_my_acc, login.login_success)

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

        services.assert_and_click(self, By.LINK_TEXT, login.login_logout)


