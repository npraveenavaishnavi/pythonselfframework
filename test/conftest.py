import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
driver =None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):                         #request is the instance it can be used to access the driver from test_end2end.py
    global driver
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        service_obj= Service("E:\chromedriver\chromedriver")
        driver=webdriver.Chrome(service=service_obj)
        driver.maximize_window()
        driver.implicitly_wait(5)
    elif browser_name=="firefox":
        service_obj = Service("E:\geckodriver-v0.32.1-win64\geckodriver")
        driver = webdriver.Firefox(service=service_obj)
        driver.maximize_window()
        driver.implicitly_wait(5)
    elif browser_name=="Edge":
        service_obj = Service("E:\edgedriver_win64\msedgedriver")
        driver = webdriver.Edge(service=service_obj)
        driver.maximize_window()
        driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver       #cls.driver is defined as class object "driver"
    yield                           #by using request instance we can pass this to main drive in the test_end2end.py file
    driver.close()