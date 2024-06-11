from features.pages.BasePage import BasePage


class YourCartPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    yourcart_lbl="//span[contains(text(),'Your Cart')]"
    checkOut_lbl= "//button[@name='checkout']"

    def click_on_Continue(self):
        self.click(self.checkOut_lbl)

    def display_status_YourCart_Page(self):
        self.isDisplayed(self.yourcart_lbl)


