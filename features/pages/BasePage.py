from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator_value):
        element = self.get_element(locator_value)
        element.click()

    def setText(self, locator_value, enter_Data):
        element = self.get_element(locator_value)
        element.send_keys(enter_Data)

    def get_element(self, locator_value):
        element = self.driver.find_element(By.XPATH, locator_value)
        return element

    def isDisplayed(self, locator_value):
        element = self.get_element(locator_value)
        return element.is_displayed()

    def scrollDown(self):
        self.driver.execute_script("window.scrollTo(0, 1080)")

    def scrollUp(self):
        self.driver.execute_script("window.scrollTo(0, 0)")





