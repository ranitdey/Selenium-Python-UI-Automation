from ptest.plogger import preporter
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeDriverManager

CHROME = "chrome"
FIREFOX = "firefox"
EDGE = "edge"


def get_new_chrome_driver():
    preporter.info("Spawning driver: Chrome")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-infobars")  # To remove automation info bar.
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.delete_all_cookies()
    driver.fullscreen_window()

    return driver


def get_new_firefox_driver():
    preporter.info("Spawning driver: FireFox")
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.delete_all_cookies()
    driver.fullscreen_window()

    return driver


def get_new_edge_driver():
    preporter.info("Spawning driver: Edge")
    driver = webdriver.Edge(EdgeDriverManager().install())
    driver.delete_all_cookies()
    driver.fullscreen_window()

    return driver
