from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .base_page import Page


class HomePage(Page):
    _home_page_text = (By.XPATH, "//span[@title='Revolut']")
    _help_tab = (By.XPATH, "//*[@id='___gatsby']/div/div[2]/div/div/div[2]/div[2]/div[4]/div[1]/span")
    _community_link = (By.XPATH, "//*[@id='___gatsby']/div/div[2]/div/div/div[2]/div[2]/div[4]/div[2]/div/div[1]/a")

    def is_home_page_open(self):
        return self._driver.find_visible_element(self._home_page_text) is not None

    def is_help_tab_displayed(self):
        return self._driver.find_visible_element(self._help_tab) is not None

    def is_community_link_displayed(self):
        return self._driver.find_visible_element(self._community_link) is not None

    def navigate_to_help_tab(self):
        self._driver.hover_over(self._help_tab)

    def click_to_community_link(self):
        self._driver.click(self._community_link)




