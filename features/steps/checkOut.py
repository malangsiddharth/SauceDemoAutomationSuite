import string
import random
import time

from behave import *

from features.pages.CheckOutComplete import CheckOutComplete
from features.pages.CheckOutInformation import CheckOutInformation
from features.pages.CheckOutPage import CheckOutPage
from features.pages.HomePage import HomePage
from features.pages.YourCartPage import YourCartPage
from features.pages.ProductPage import ProductPage
from features.pages.BasePage import BasePage


@given(u'Login into application')
def loginIntoApplication(context):
    context.home_page = HomePage(context.driver)
    username = "standard_user"
    password = "secret_sauce"
    assert True.__eq__(context.home_page.display_status_HomePage())
    context.home_page.enterDataUsername(data=username)
    context.home_page.enterDataPassword(data=password)
    context.home_page.click_on_login()


@when(u'Select three random items')
def selectThreeRandomItems(context):
    context.product_page = ProductPage(context.driver)
    assert True.__eq__(context.product_page.display_status_Product_Page())
    range_list=[*range(1, 7, 1)]
    product_listToSelect=(random.sample(range_list, 3))
    for i in range(3):
       if(product_listToSelect[i]>4):
            context.base_page = BasePage(context.driver)
            context.base_page.scrollDown()
            time.sleep(3)
            context.product_page.selectDynamicElement(product_listToSelect[i])
            time.sleep(3)
            context.base_page.scrollUp()
       else:
           context.base_page = BasePage(context.driver)
           context.base_page.scrollUp()
           context.product_page.selectDynamicElement(product_listToSelect[i])
    assert "3".__eq__(context.product_page.getelement())
    context.product_page.clickOnShoppingIcon()

@when(u'View My Cart')
def ypurCartPageImplementation(context):
    context.yourCart_Page=YourCartPage(context.driver)
    assert True.__eq__(context.yourCart_Page.display_status_YourCart_Page())
    context.yourCart_Page.click_on_Continue()


@then(u'Add Address')
def addAddress(context):
    fname_random = ''.join(random.choices("FNAME" + string.ascii_uppercase, k=3))
    lname_random = ''.join(random.choices("LNAME" + string.ascii_uppercase, k=3))
    postalCode_random = random.choices(string.digits, k=6)
    context.checkOutInformation_Page=CheckOutInformation(context.driver)
    assert True.__eq__(context.checkOutInformation_Page.display_status_CheckOutInformation_Page())
    context.checkOutInformation_Page.enterDataFirstName(fname_random)
    context.checkOutInformation_Page.enterDataLastName(lname_random)
    context.checkOutInformation_Page.enterDataPinCode(postalCode_random)
    context.checkOutInformation_Page.click_on_Continue()


@when(u'CheckOut the order')
def CheckOutOverview(context):
    context.checkOutOverview_Page = CheckOutPage(context.driver)
    assert True.__eq__(context.checkOutOverview_Page.display_CheckOutOverview())
    context.checkOutOverview_Page.clickOnFinish()


@then(u'Complete order')
def step_impl(context):
    context.checkOutComplete_Page = CheckOutComplete(context.driver)
    assert True.__eq__(context.checkOutComplete_Page.display_status_checkOutComplete_lbl())
    assert True.__eq__(context.checkOutComplete_Page.display_status_orderConfirmation_lbl())
    assert True.__eq__(context.checkOutComplete_Page.display_status_dispatched_lbl())
