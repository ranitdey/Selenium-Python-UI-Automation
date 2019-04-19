from ptest.decorator import BeforeClass, AfterClass, TestClass
from ptest.plogger import preporter
from utils.driver_utils import FIREFOX
from utils.selenium_driver import SeleniumDriver


@TestClass()
class BaseTest:

    @BeforeClass()
    def setup(self):
        self._driver = SeleniumDriver()
        self.initialize_pages(self._driver)

    # @AfterClass()
    # def tear_down(self):
    #     preporter.info("Closing driver")
    #     self._driver.get_driver().close()
    #     self._driver.get_driver().quit()

    def initialize_pages(self, driver):
        from ..pages.home_page import HomePage
        self._home_page = HomePage(driver)

        from ..pages.community_page import CommunityPage
        self._community_page = CommunityPage(driver)


