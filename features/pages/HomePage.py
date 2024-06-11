

from features.pages.BasePage import BasePage

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    username_txtbox = "//input[@name='user-name']"
    password_txtbox = "//input[@name='password']"
    login_button = "//input[@name='login-button']"
    title_lbl = "//div[text()='Swag Labs']"

    def click_on_login(self):
        self.click(self.login_button)

    def enterDataUsername(self,data):
        self.setText(self.username_txtbox,data)

    def enterDataPassword(self, data):
        self.setText(self.password_txtbox, data)

    def display_status_HomePage(self):
        self.isDisplayed(self.title_lbl)

