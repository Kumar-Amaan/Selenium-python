from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']/div/h4")
    # cardText = (By.XPATH, "div/h4")
    addToCartBtn = (By.XPATH, "//div[@class='card h-100']/div/button")
    checkoutLink = (By.PARTIAL_LINK_TEXT, "Checkout")


    def getCardTitle(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getAddCartBtn(self):
        return self.driver.find_element(*CheckoutPage.addToCartBtn)

    def getCheckoutLink(self):
        self.driver.find_element(*CheckoutPage.checkoutLink).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage



