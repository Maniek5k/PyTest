# This is testing that product isn't added to wishlist while not logged in
# Customer won't get access via. direct link to wishlist, will be redirected to login page
from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_wishlist import wishlist
from pages.page_login import login


class TestWishlistFail(Base):
    def test_wishlist_fail(self):
        self.driver.get(wishlist.wishlist_pp)

        services.assert_and_click(self, By.XPATH, wishlist.wishlist_add)

        self.driver.get(wishlist.wishlist_acc_page)

        assert self.driver.current_url == login.login_url
