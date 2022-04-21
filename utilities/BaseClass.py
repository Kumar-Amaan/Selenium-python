import datetime
import inspect
import logging
import time
from datetime import date, timedelta

import pytest
import xlrd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def waitForLinkText(self, link):
        wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, link)))

    def scrollBottom(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)

    def scrollUp(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    # def data(self, days):
    #     CurrentDate = datetime.date.today(days)
    #     # %d is for date
    #     # %b is for month
    #     # Y is for Year
    #     print(CurrentDate.strftime('%d-%m-%Y'))

    def selectValuesFromDropDown(self, dropDownList, value):
        print(len(dropDownList))
        for ele in dropDownList:
            print(ele.text)
            if ele.text == value:
                ele.click()
                break
