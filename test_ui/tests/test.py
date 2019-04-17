from ptest.decorator import TestClass, Test
from ptest.plogger import preporter
import config
from test_ui.tests.base_test import BaseTest
from ptest.assertion import assert_equals


@TestClass(run_mode='singleline', description="Test Case")
class CreativeUITests(BaseTest):

    @Test(description="Check if topics gets populated in search and its title ")
    def tc_001_login_test(self):
        target_text = "We got a banking licence"
        preporter.info("Open URL: " + config.base_ui_url)
        self._driver.open_url(config.base_ui_url)
        self._home_page.navigate_to_help_tab()
        self._home_page.click_to_community_link()
        self._driver.switch_window()
        self._community_page.search_text(target_text)
        self._community_page.click_on_first_search_item()
        assert_equals(self._community_page.get_topic_title(), target_text, "Expected topic not found")




