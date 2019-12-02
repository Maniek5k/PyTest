# Test for adding to wishlist

import time

from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_wishlist import wishlist
from pages.page_login import login


class TestWishlistAdd(Base):
    def test_wishlist_add(self):
        self.driver.get(login.login_url)

        services.send_keys_by_xpath(self, login.login_mail_input, wishlist.wishlist_mail)

        login.check_login(self)

        self.driver.get(wishlist.wishlist_pp)

        services.assert_and_click(self, By.XPATH, wishlist.wishlist_add)
        time.sleep(1)

        services.is_element_visible(self, By.CSS_SELECTOR, wishlist.wishlist_add_success)

        self.driver.get(wishlist.wishlist_acc_page)

        services.is_element_visible(self, By.CSS_SELECTOR, wishlist.wishlist_table)

        services.assert_and_click(self, By.CSS_SELECTOR, wishlist.wishlist_remove)

        services.assert_text(self, By.CSS_SELECTOR, wishlist.wishlist_rm_success, wishlist.wishlist_rm_text)

        login.check_logout(self)