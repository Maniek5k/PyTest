# Test for checking checkout process with out of stock product

import time

from selenium.webdriver.common.by import By

from conftest import Base, services
from pages.page_basket import basket
from pages.page_checkout import checkout
from pages.page_login import login


class TestCheckout(Base):
    def test_checkout(self):
        self.driver.get(basket.basket_oos_pp)

        services.assert_and_click(self, By.XPATH, basket.basket_add)

        services.assert_and_click(self, By.XPATH, basket.basket_cart)

        services.assert_text(self, By.CSS_SELECTOR, basket.basket_oos_product, basket.basket_oos_msg)

        services.assert_and_click(self, By.CSS_SELECTOR, basket.basket_remove)
        time.sleep(1)
        services.assert_text(self, By.XPATH, basket.basket_empty, basket.basket_empty_text)
