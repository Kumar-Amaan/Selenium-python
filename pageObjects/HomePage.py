from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")

    def getShopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(By.XPATH, "//label[text()='Name']/..//input")

    def getEmail(self):
        return self.driver.find_element(By.XPATH, "//label[text()='Email']/..//input")

    def getPassword(self):
        return self.driver.find_element(By.XPATH, "//label[text()='Password']/..//input")

    def getCheckMe(self):
        return self.driver.find_element(By.XPATH, "//div[@class='form-check']/input")

    def getGender(self):
        return self.driver.find_element(By.XPATH, "//label[text()='Gender']/..//select")

    def getEmployementStatus(self):
        return self.driver.find_element(By.XPATH, "//label[text()='Employment Status: ']/..//div/label[text()='Employed']")

    def getDOB(self):
        return self.driver.find_element(By.XPATH, "//label[text()='Date of Birth']/..//input")

    def getSubmitBtn(self):
        return self.driver.find_element(By.XPATH, "//input[@type='submit']")

    def getSuccessMessage(self):
        return self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

