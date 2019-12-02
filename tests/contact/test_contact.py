# Test checking that contact form works correctly

from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_contact import contact


class TestContact(Base):
    def test_contact(self):
        services.assert_and_click(self, By.LINK_TEXT, contact.contact_link)

        services.send_keys_by_xpath(self, contact.contact_name, contact.contact_data_name)

        services.send_keys_by_xpath(self, contact.contact_mail, contact.contact_data_mail)

        services.send_keys_by_xpath(self, contact.contact_message, contact.contact_data_short_message)

        services.assert_and_click(self, By.XPATH, contact.contact_submit)

        services.assert_text(self, By.XPATH, contact.contact_success, contact.contact_success_text)