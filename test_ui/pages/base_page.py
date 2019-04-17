
class Page:
    """This class contains the basic actions for all the pages."""
    EXPLICIT_WAIT_TIME = 10

    def __init__(self, driver):
        self._driver = driver
        self._driver.set_explicit_wait_time(self.EXPLICIT_WAIT_TIME)