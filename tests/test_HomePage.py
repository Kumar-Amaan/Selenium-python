import time

import pytest
from selenium.webdriver.support.select import Select

from TestData.ExcelReader import ExcelReader
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("Entering Name")
        homepage.getName().send_keys(getData["name"])
        log.info("Entering Email")
        homepage.getEmail().send_keys(getData["email"])
        log.info("Entering Password")
        homepage.getPassword().send_keys(getData["password"])
        log.info("Clicking on checkbox")
        homepage.getCheckMe().click()
        log.info("Selecting gender")
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        log.info("Choosing employement status radio btn")
        homepage.getEmployementStatus().click()
        log.info("Entering date of birth")
        homepage.getDOB().send_keys(self.gateDatefromToday(3))
        time.sleep(2)
        log.info("Clicking Submit btn")
        homepage.getSubmitBtn().click()
        time.sleep(2)
        log.info("Scrolling up")
        self.scrollUp()
        msg = homepage.getSuccessMessage().text
        assert ("submitted successfully!." in msg)
        self.driver.refresh()

    @pytest.fixture(params=ExcelReader.getTestData("TC02"))
    def getData(self, request):
        return request.param

