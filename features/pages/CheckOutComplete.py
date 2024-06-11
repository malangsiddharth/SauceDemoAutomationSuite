from features.pages.BasePage import BasePage


class CheckOutComplete(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    checkOutComplete_lbl="//span[text()='Checkout: Complete!']"
    orderconfirmation_lbl= "//h2[text()='Thank you for your order!']"
    dispatched_lbl="//div[text()='Your order has been dispatched, and will arrive just as fast as the pony can get there!']"

    def display_status_checkOutComplete_lbl(self):
        self.isDisplayed(self.checkOutComplete_lbl)

    def display_status_orderConfirmation_lbl(self):
        self.isDisplayed(self.orderconfirmation_lbl)

    def display_status_dispatched_lbl(self):
        self.isDisplayed(self.dispatched_lbl)


