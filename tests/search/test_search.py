# Test for general search engine testing

from selenium.webdriver.common.by import By

from conftest import Base
from conftest import services
from pages.page_search import search


class TestSearchSuccess(Base):
    def test_search(self):
        services.send_keys_by_xpath(self, search.search_input, search.search_case)

        services.assert_and_click(self, By.XPATH, search.search_submit)

        services.assert_text(
            self, By.LINK_TEXT, search.search_result, search.search_case
        )

        # services.clear_element_by_xpath(self, search.search_input)

        # services.assert_and_click(self, By.XPATH, search.search_submit)

        # services.assert_text(
        #     self, By.XPATH, search.search_failed, search.search_failed_msg
        # )