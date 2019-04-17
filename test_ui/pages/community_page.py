from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .base_page import Page


class CommunityPage(Page):
    _search = (By.XPATH, "//*[@id='search-button']")
    _search_text = (By.XPATH, "//*[@id='search-term']")
    _first_search_item = (By.XPATH, "//*[@id='ember6']/header/div/div/div[2]/div/div/div/div/div[3]/div/div/ul/li[1]")
    _topic_title = (By.XPATH, "//*[@id='topic-title']/div/div/h1/a[2]")

    def is_search_displayed(self):
        return self._driver.find_visible_element(self._search) is not None

    def navigate_to_help_tab(self):
        self._driver.hover_over(self._help_tab)

    def click_on_search(self):
        self._driver.click(self._search)

    def search_text(self, text):
        self.click_on_search()
        self._driver.send_keys(self._search_text, text)

    def click_on_first_search_item(self):
        self._driver.click(self._first_search_item)

    def get_topic_title(self):
        return self._driver.find_visible_element(self._topic_title).text
