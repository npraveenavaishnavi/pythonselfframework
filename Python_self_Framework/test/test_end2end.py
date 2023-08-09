from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from pageObject.Homepage import HomePage
from pageObject.checkoutpage import CheckOutPage
from test.utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setupbrowser")

@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_end2end(self):
        homepage = HomePage(self.driver)
        homepage.shopitems().click()
        # self.driver.find_element(By.CSS_SELECTOR, " a[href*='shop']").click()
        checkoutpage = CheckOutPage(self.driver)
        # self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        products = checkoutpage.getproductsTitles()
        print (products)
        for product in products:
            #productName=checkoutpage.getproductName()
            productName=checkoutpage.getproductName().text
            if productName == "Nokia Edge":
                #self.driver.find_element(By.XPATH,"//app-card[4]//div[1]//div[2]//button[1]").click()
                checkoutpage.getaddButton().click()
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[class='btn btn-success btn-lg']").click()
        SuccessText = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        assert "Success! Thank you!" in SuccessText
        # self.driver.close()
