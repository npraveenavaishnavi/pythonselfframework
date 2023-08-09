import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObject.Homepage import HomePage
from test.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):

        #service_obj = Service("E:\chromedriver\chromedriver")
        #driver = webdriver.Chrome(service=service_obj)
        #driver.get("https://rahulshettyacademy.com/angularpractice/")
        #driver.maximize_window()
        log=self.getLogger()
        homepage=HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getPassword().send_keys("123456")
        homepage.getCheckbox().click()
        self.selectOptionByText(homepage.getGender(),getData["gender"])
        #dropdown.select_by_visible_text("Female")
        homepage.getSubmit().click()
        alertText=homepage.getSuccessmsg().text
        assert ("success" in alertText)
        #self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self,request):
        return request.param