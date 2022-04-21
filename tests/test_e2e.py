import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# @pytest.mark.usefixtures("setup")
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkout = homePage.getShopItems()
        # log.info("getting all the card titles")
        cards = checkout.getCardTitle()
        log.info("Getting all catd Titles")
        i = -1
        for card in cards:
            # i = i + 1
            cardText = card.text
            log.info("Getting Card text")
            print("Card Text::::::::::::::::>>>>>>", cardText)
            log.info(cardText)
            if cardText == "Blackberry":
                checkout.getAddCartBtn().click()

        time.sleep(1)
        log.info("Clicking on Checkout Link")
        confirmPage = checkout.getCheckoutLink()
        time.sleep(2)
        confirmPage.getCheckoutBtn().click()
        log.info("Clicking on Checkout Button")
        time.sleep(2)
#         perform actions in dropdown and checkbox
        countryDropdown = confirmPage.getCountryDropdown()
        countryDropdown.click()
        log.info("entering country name")
        countryDropdown.send_keys("ind")

        self.waitForLinkText("India")
        log.info("clicking on country name")
        confirmPage.getCountry().click()
        time.sleep(2)
        log.info("Clicking on checkbox")
        confirmPage.getCheckBox().click()
        log.info("Clicking on Purchase button")
        confirmPage.getPurchaseBtn().click()
        time.sleep(2)
        successMsg = confirmPage.getSuccessMessage().text
        log.info("Verifying message text")
        assert ("Success! Thank you" in successMsg)
#         get Screenshot
        self.driver.get_screenshot_as_file("screenshot.png")



