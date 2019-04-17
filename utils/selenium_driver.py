import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from ptest.plogger import preporter
from utils import driver_utils


class SeleniumDriver:
    _explicit_wait_time = 0

    def __init__(self, browser_type=driver_utils.CHROME):    # default browser is chrome if no browser_type is provided
        if browser_type == driver_utils.CHROME:
            self._driver = driver_utils.get_new_chrome_driver()
        elif browser_type == driver_utils.FIREFOX:
            self._driver = driver_utils.get_new_firefox_driver()
        elif browser_type == driver_utils.EDGE:
            self._driver = driver_utils.get_new_edge_driver()

        else:
            preporter.critical("The browser type specified ({browser_type}) is not supported by the framework."
                               .format(browser_type=browser_type))
            assert False    # Stopping the test.

    def open_url(self, url):
        self._driver.get(url)

    def switch_window(self):
        self._driver.switch_to.window(self._driver.window_handles[len(self.get_window_handlers())-1])

    def get_window_handlers(self):
        return self._driver.window_handles

    def get_driver(self):
        return self._driver

    def set_explicit_wait_time(self, explicit_wait_time):
        self._explicit_wait_time = explicit_wait_time

    def find_visible_element(self, locator, wait_until=None):
        preporter.info("Finding visible element: " + (str(locator)))
        wait_until = self._explicit_wait_time if wait_until is None else wait_until
        element = WebDriverWait(self._driver, wait_until).until(
            EC.visibility_of_element_located(locator)
        )
        return element

    def wait_for_element_to_disappear(self, locator, wait_until=None):
        preporter.info("Waiting for invisibility of element: " + str(locator))
        wait_until = self._explicit_wait_time if wait_until is None else wait_until
        element = WebDriverWait(self._driver, wait_until).until(
            EC.invisibility_of_element_located(locator)
        )
        return element

    def find_clickable_element(self, locator, wait_until=None):
        preporter.info("Finding clickable element: " + (str(locator)))
        wait_until = self._explicit_wait_time if wait_until is None else wait_until
        element = WebDriverWait(self._driver, wait_until).until(
            EC.element_to_be_clickable(locator)
        )
        return element

    def click(self, locator, wait_until=None):
        preporter.info("Clicking element: " + (str(locator)))
        wait_until = self._explicit_wait_time if wait_until is None else wait_until
        self.find_visible_element(locator, wait_until)  # Ignoring the returned element
        element = self.find_clickable_element(locator, wait_until)
        self._driver.execute_script("return arguments[0].scrollIntoView();", element)
        try:
            element.click()
        except WebDriverException as wde:
            if "Other element would" in wde.msg or "not attached" in wde.msg:
                time.sleep(2)   # Wait two seconds before trying again.
                element.click()

    def send_keys(self, locator, text, wait_until=None):
        preporter.info("Sending text '" + str(text) + "' to element: " + (str(locator)))
        wait_until = self._explicit_wait_time if wait_until is None else wait_until
        element = self.find_clickable_element(locator, wait_until)
        self._driver.execute_script("return arguments[0].scrollIntoView();", element)
        element.click()
        element.clear()
        element.send_keys(text)

    def hover_over(self, locator, wait_until=None):
        preporter.info("Hovering over element: " + (str(locator)))
        wait_until = self._explicit_wait_time if wait_until is None else wait_until
        element = self.find_visible_element(locator, wait_until)
        self._driver.execute_script("return arguments[0].scrollIntoView();", element)
        hover_action = ActionChains(self.get_driver()).move_to_element(element)
        hover_action.perform()

