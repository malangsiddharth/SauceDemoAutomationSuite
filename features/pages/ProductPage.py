from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    product_lbl = "//span[text()='Products']"
    inventory_lbls = "//div[contains(@class,'inventory_item_name')]"
    shoppingCart_icon = "//span[@class='shopping_cart_badge']"
    product_element = "(//button[contains(text(),'Add to cart')])[X]"
    noOfProductAddedToCart_icn="//span[@class='shopping_cart_badge']"

    def display_status_Product_Page(self):
        self.isDisplayed(self.product_lbl)

    def clickOnShoppingIcon(self):
        self.click(self.shoppingCart_icon)

    def selectDynamicElement(self, item_idx):
        modify_xpath = self.product_element.replace("X", str(item_idx))
        self.click(modify_xpath)

    def getelement(self):
        self.get_element(self.noOfProductAddedToCart_icn)
