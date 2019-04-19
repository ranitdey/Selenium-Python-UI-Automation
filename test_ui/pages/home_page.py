from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .base_page import Page
from ptest.plogger import preporter


class HomePage(Page):

    _home_page_text = (By.XPATH, "//span[@title='Revolut']")
    _help_tab = (By.XPATH, "//div[contains(@class, 'styles__StyledRightPart')]/div[4]/div[1]/span")
    _community_link = (By.XPATH, "//div[contains(@class, 'styles__StyledRightPart')]/div[4]/div[2]/div[1]/div[1]/a")
    _all_countries_flag = (By.XPATH, "//*[@id='___gatsby']/div/div[5]/div/div[3]/div/div[2]/div/button")
    _current_selected_country = (By.XPATH, "//*[@id='___gatsby']/div/div[5]/div/div[3]/div/div/div[2]")
    _search_countries_available = (By.XPATH, "//*[@id='___gatsby']/div/div[5]/div/div[3]/div/div[2]/label/input")
    _first_search_item = (By.XPATH, "//*[@id='___gatsby']/div/div[5]/div/div[3]/div/div[2]/div/button[1]/a/div[2]")
    _hiring_banner = (By.XPATH, "//*[@id='___gatsby']/div/div[4]/div/a/div")

    def is_home_page_open(self):
        return self._driver.find_visible_element(self._home_page_text) is not None

    def click_on_homepage(self):
        self._driver.click(self._home_page_text)

    def is_help_tab_displayed(self):
        return self._driver.find_visible_element(self._help_tab) is not None

    def is_community_link_displayed(self):
        return self._driver.find_visible_element(self._community_link) is not None

    def navigate_to_help_tab(self):
        self._driver.hover_over(self._help_tab)

    def click_to_community_link(self):
        self._driver.click(self._community_link)

    def click_on_current_selected_country(self):
        self._driver.click(self._current_selected_country)

    def get_current_selected_country_name(self):
        return self._driver.click(self._current_selected_country).text

    def get_all_countries_name(self):
        self.countries = self._driver.find_visible_elements(self._all_countries_flag)
        self.country_names = []
        for i in self.countries:
            self.country_names.append(i.text)
        return self.country_names

    def search_in_available_countries(self,text):
        self._driver.send_keys(self._search_countries_available, text)

    def click_on_first_search_item(self):
        self._driver.click(self._first_search_item)

    def click_on_hiring_banner(self):
        self._driver.click(self._hiring_banner)








