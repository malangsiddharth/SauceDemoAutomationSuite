from features.pages.BasePage import BasePage


class CheckOutInformation(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    firstname_txtbox="//input[@name='firstName']"
    lastname_txtbox="//input[@name='lastName']"
    pincode_txtbox="//input[@name='postalCode']"
    continue_btn="//input[@name='continue']"
    checkoutInformation_lbl="//span[contains(text(),'Checkout: Your Information')]"

    def click_on_Continue(self):
        self.click(self.continue_btn)

    def enterDataFirstName(self, data):
        self.setText(self.firstname_txtbox, data)

    def enterDataLastName(self, data):
        self.setText(self.lastname_txtbox, data)

    def enterDataPinCode(self, data):
        self.setText(self.pincode_txtbox, data)

    def display_status_CheckOutInformation_Page(self):
        self.isDisplayed(self.checkoutInformation_lbl)


