# Test checking for correct error message if checkbox on register form isn't checked

from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_register import register


class TestRegisterPP(Base):
    def test_register_pp(self):
        self.driver.get(register.register_url)

        services.assert_and_click(self, By.CSS_SELECTOR, register.register_btn)

        services.assert_and_click(self, By.CSS_SELECTOR, register.register_submit)

        services.assert_text(
            self, By.CSS_SELECTOR, register.register_alert, register.register_policy
        )
