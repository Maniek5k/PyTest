# Test for adding gift card to basket

import time

from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_basket import basket


class TestGcAdd(Base):
    def test_gc_add(self):
        services.assert_and_click(self, By.LINK_TEXT, basket.basket_gc)

        services.send_keys_by_xpath(self, basket.basket_gc_name, basket.basket_gc_data)

        services.send_keys_by_xpath(self, basket.basket_gc_mail, basket.basket_gc_data_mail)

        services.send_keys_by_xpath(self, basket.basket_gc_sender_name, basket.basket_gc_data)

        services.send_keys_by_xpath(self, basket.basket_gc_sender_mail, basket.basket_gc_data_mail)

        services.assert_and_click(self, By.XPATH, basket.basket_gc_radio)

        services.assert_and_click(self, By.XPATH, basket.basket_gc_submit)

        services.assert_text(self, By.CSS_SELECTOR, basket.basket_gc_alert_fail, basket.basket_gc_fail_text)

        services.assert_and_click(self, By.NAME, basket.basket_gc_checkbox)

        services.assert_and_click(self, By.XPATH, basket.basket_gc_submit)

        services.assert_and_click(self, By.LINK_TEXT, basket.basket_gc_continue)

        services.assert_and_click(self, By.CSS_SELECTOR, basket.basket_remove)
        time.sleep(1)
        services.assert_text(self, By.XPATH, basket.basket_empty, basket.basket_empty_text)