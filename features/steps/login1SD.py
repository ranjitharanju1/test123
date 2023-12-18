from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('I launch the browser')
def launchbrowser(context):
    context.driver = webdriver.Chrome()


@when('open Saucedemo home page')
def openloginpage(context):
    context.driver.get("https://www.saucedemo.com/")
    time.sleep(4)

@then('I verify that the SwagLabs text present on page')
def verifylogo(context):
    status = context.driver.find_element(By.XPATH, "//div[contains(text(),'Swag Labs')]").is_displayed()
    assert status is True

@then('I close the browser')
def closebrowser(context):
    context.driver.close()


@then('Enter username "{user}" and password "{pwd}"')
def enterusernamepwd(context, user, pwd):
    context.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(user )
    context.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(pwd)
    time.sleep(4)

@then('Click on login button')
def clicklogin(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(4)

@then('user must successfully login to the product pageAnd I close the browser')
def productpagedisplay(context):
    assert context.driver.find_element(By.XPATH, "//span[contains(text(),'Products')]").is_displayed()
    time.sleep(4)


@then('click on add to cart button for selected product')
def clickaddtocart(context):
    context.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
    time.sleep(4)


@then('click on cart icon')
def clickcart(context):
    context.driver.find_element(By.XPATH, "//body/div[@id='root']/div[@id='page_wrapper']/div[@id='contents_wrapper']/div[@id='header_container']/div[1]/div[3]/a[1]").click()
    time.sleep(4)

@then('product should be visible in the your cart page')
def cartpagedisplay(context):
    assert context.driver.find_element(By.XPATH, "//span[contains(text(),'Your Cart')]   ").is_displayed()
    time.sleep(4)

@then('click on the checkout button')
def clickcheckout(context):
    context.driver.find_element(By.XPATH, "//button[@id='checkout']").click()
    time.sleep(4)

@then('user should be navigated to checkout your information page')
def informationdisplay(context):
    assert context.driver.find_element(By.XPATH, "//span[contains(text(),'Checkout: Your Information')]").is_displayed()
    time.sleep(4)


@then('enter firstname "{fname}" and lastname "{lname}" and postalcode "{pcode}"')
def enterfnamelnamepcode(context, fname, lname, pcode):
    context.driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys(fname)
    context.driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys(lname)
    context.driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys(pcode)
    time.sleep(4)


@then('click on continue button')
def clickcontinue(context):
    context.driver.find_element(By.XPATH, "//input[@id='continue']").click()
    time.sleep(4)


@then('user should be navigated to checkout overview page')
def overviewpagedisplay(context):
    assert context.driver.find_element(By.XPATH, "//span[contains(text(),'Checkout: Overview')]").is_displayed()
    time.sleep(4)


@then('click on finish button')
def clickfinish(context):
    context.driver.find_element(By.XPATH, "//button[@id='finish']").click()
    time.sleep(4)


@then('user must navigated to checkout complete page')
def completepagedisplay(context):
    assert context.driver.find_element(By.XPATH, "//span[contains(text(),'Checkout: Complete!')]").is_displayed()
    time.sleep(4)


@then('click on backhome button')
def clickbackhome(context):
    context.driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()
    time.sleep(4)


@then('user must navigated to the product page')
def productpagedisplay(context):
    assert context.driver.find_element(By.XPATH, "//span[contains(text(),'Products')]").is_displayed()
    time.sleep(4)
