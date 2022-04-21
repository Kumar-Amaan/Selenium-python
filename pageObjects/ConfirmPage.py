from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    countryDropdown = (By.XPATH, "//label[contains(text(),'Please choose')]/..//input")
    country = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseBtn = (By.XPATH, "//div[@class='checkbox checkbox-primary']/..//input[@value='Purchase']")
    successMessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    checkoutBtn = (By.XPATH, "//button[contains(text(),'Checkout')]")

    def getCheckoutBtn(self):
        return self.driver.find_element(*ConfirmPage.checkoutBtn)

    def getCountryDropdown(self):
        return self.driver.find_element(*ConfirmPage.countryDropdown)

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getPurchaseBtn(self):
        return self.driver.find_element(*ConfirmPage.purchaseBtn)

    def getSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.successMessage)
