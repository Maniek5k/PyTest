# Test trying to add product, which cannot be added due to not all required options chosen

import time

from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_basket import basket


class TestBasketCannotAdd(Base):
    def test_basket_cannot_add(self):
        self.driver.get(basket.basket_cannot_pp)

        services.assert_and_click(self, By.XPATH, basket.basket_add)
        time.sleep(1)
        services.assert_text(self, By.CSS_SELECTOR, basket.basket_cannot_alert, basket.basket_cannot_alert_text)