import time

from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_basket import basket
from pages.page_login import login


class TestBasketReorder(Base):
    def test_basket_reorder(self):
        self.driver.get(login.login_url)

        services.send_keys_by_xpath(self, login.login_mail_input, basket.reorder_mail)

        services.send_keys_by_xpath(self, login.login_pwd_input, basket.reorder_pwd)

        services.assert_and_click(self, By.CSS_SELECTOR, login.login_submit)

        services.assert_text(self, By.XPATH, login.login_my_acc, login.login_success)

        services.assert_and_click(self, By.LINK_TEXT, basket.reorder_history)

        services.assert_and_click(self, By.CSS_SELECTOR, basket.reorder_view)

        services.assert_and_click(self, By.CSS_SELECTOR, basket.reorder_add)

        services.is_element_visible(self, By.CSS_SELECTOR, basket.reorder_success)

        services.assert_and_click(self, By.XPATH, basket.basket_cart)

        services.assert_and_click(self, By.CSS_SELECTOR, basket.basket_remove)
        time.sleep(1)
        services.is_element_visible(self, By.XPATH, basket.basket_empty)

        services.assert_text(self, By.XPATH, basket.basket_empty, basket.basket_empty_text)

        self.driver.get(login.login_url)

        services.assert_and_click(self, By.LINK_TEXT, login.login_logout)

        services.assert_text(self, By.XPATH, login.logout_success, login.logout_success_text)