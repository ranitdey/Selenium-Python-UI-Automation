from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .base_page import Page


class CommunityPage(Page):

    _search = (By.XPATH, "//a[@id='search-button']")
    _search_text = (By.XPATH, "//input[@id='search-term']")
    _first_search_item = (By.XPATH, "//div[@class='search-menu']//li[1]")
    _search_results_titles_first_order = (By.XPATH, "//div[@class='search-menu']//span[@class='topic-title']")
    _topic_title = (By.XPATH, "//a[@class='fancy-title']")
    _hamburger_menu = (By.XPATH, "//a[@id='toggle-hamburger-menu']")
    _keyboard_shortcuts = (By.XPATH, "//span[contains(text(),'Keyboard Shortcuts')]")

    def is_search_displayed(self):
        return self._driver.find_visible_element(self._search) is not None

    def is_keyboard_shortcuts_displayed(self):
        return self._driver.find_visible_element(self._keyboard_shortcuts) is not None

    def click_on_keyboard_shortcuts(self):
        self._driver.click(self._keyboard_shortcuts)

    def navigate_to_help_tab(self):
        self._driver.hover_over(self._help_tab)

    def click_on_search(self):
        self._driver.click(self._search)

    def click_on_hamburger_menu(self):
        self._driver.click(self._hamburger_menu)

    def search_text(self, text):
        self.click_on_search()
        self._driver.send_keys(self._search_text, text)

    def click_on_first_search_item(self):
        self._driver.click(self._first_search_item)

    def get_topic_title(self):
        return self._driver.find_visible_element(self._topic_title).text

    def get_first_order_search_results_titles(self):
        self.search_results_elements = self._driver.find_visible_elements(self._search_results_titles_first_order)
        self.search_results = []
        for result in self.search_results_elements:
            self.search_results.append(result.text)
        return self.search_results
