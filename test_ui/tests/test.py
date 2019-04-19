
from ptest.decorator import TestClass, Test
from ptest.plogger import preporter
import config
from test_ui.tests.base_test import BaseTest
from ptest.assertion import assert_equals, assert_list_elements_equal, assert_true
from selenium.common.exceptions import TimeoutException, WebDriverException
from ..test_data.countries_data import available_countries, countries_to_url_map


@TestClass(run_mode='singleline', description="Test Case")
class UITests(BaseTest):

    @Test(description="Check if topics gets populated in search and its title is proper")
    def tc_001_topic_title_test(self):
        target_text = "We got a banking licence"
        preporter.info("Opening URL: " + config.base_ui_url)
        self._driver.open_url(config.base_ui_url)
        self._home_page.navigate_to_help_tab()
        self._home_page.click_to_community_link()
        self._driver.switch_window()
        self._community_page.search_text(target_text)
        self._community_page.click_on_first_search_item()
        assert_equals(self._community_page.get_topic_title(), target_text, "Expected topic not found")

    @Test(description="Check all available country flags")
    def tc_002_available_country_test(self):
        preporter.info("Opening URL: " + config.base_ui_url)
        self._driver.open_url(config.base_ui_url)
        try:
            self._home_page.click_on_current_selected_country()
            assert_list_elements_equal(self._home_page.get_all_countries_name(), available_countries,
                                       "All country flags did't matched")
        except (TimeoutException, WebDriverException):
            self._home_page.click_on_hiring_banner()              # TODO Find a better method to handle the banner
            self._home_page.click_on_homepage()
            self._home_page.click_on_current_selected_country()
            assert_list_elements_equal(self._home_page.get_all_countries_name(), available_countries,
                                       "All country flags did't matched")

    @Test(data_provider=available_countries, description="Check all available country flags and its url")
    def tc_003_available_countries_url_test(self, country):
        preporter.info("Opening URL: " + config.base_ui_url)
        self._driver.open_url(config.base_ui_url)
        try:
            self._home_page.click_on_current_selected_country()
            self._home_page.search_in_available_countries(country)
            self._home_page.click_on_first_search_item()
            preporter.info("Searching for country: " + country)
            preporter.info("Matching with URL: " + self._driver.get_url())
            assert_equals(self._driver.get_url(), countries_to_url_map[country],
                          "URL did't match with country code: " + country)
        except (TimeoutException, WebDriverException):

            self._home_page.click_on_hiring_banner()              # TODO Find a better method to handle the banner
            self._home_page.click_on_homepage()
            self._home_page.click_on_current_selected_country()
            self._home_page.search_in_available_countries(country)
            self._home_page.click_on_first_search_item()
            preporter.info("Searching for country: " + country)
            preporter.info("Matching with URL: " + self._driver.get_url())
            assert_equals(self._driver.get_url(), countries_to_url_map[country],
                          "URL did't match with country code: " + country)

    @Test(description="Check if keyboard_shortcuts button is displayed in community page")
    def tc_004_keyboard_shortcut_test(self):
        preporter.info("Opening URL: " + config.base_ui_url)
        self._driver.open_url(config.base_ui_url)
        self._home_page.navigate_to_help_tab()
        self._home_page.click_to_community_link()
        self._driver.switch_window()
        self._community_page.click_on_hamburger_menu()
        assert_true(self._community_page.is_keyboard_shortcuts_displayed(), "Keyboard shortcut button not displayed")




