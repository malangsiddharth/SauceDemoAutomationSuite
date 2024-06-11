
from features.pages.BasePage import BasePage

class CheckOutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    checkOutOverview_lbl="//span[text()='Checkout: Overview']"
    checkOut_lbl= "//button[@name='finish']"

    def clickOnFinish(self):
        self.click(self.checkOut_lbl)

    def display_CheckOutOverview(self):
        self.isDisplayed(self.checkOutOverview_lbl)

