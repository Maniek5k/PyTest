# Test for successful adding product to basket and checking if correct product was added

import time

from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_basket import basket


class TestBasketAdd(Base):
    def test_basket_add(self):
        self.driver.get(basket.basket_pp)

        pp_name = services.get_text(self, By.CSS_SELECTOR, basket.basket_name)

        services.assert_and_click(self, By.XPATH, basket.basket_add)

        services.assert_and_click(self, By.XPATH, basket.basket_cart)

        cart_name = services.get_text(self, By.XPATH, basket.basket_cart_name)

        assert cart_name == pp_name

        services.assert_and_click(self, By.CSS_SELECTOR, basket.basket_remove)
        time.sleep(1)
        services.assert_text(self, By.XPATH, basket.basket_empty, basket.basket_empty_text)
