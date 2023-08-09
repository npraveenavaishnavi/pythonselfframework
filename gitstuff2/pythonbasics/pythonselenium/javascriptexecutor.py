from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#to run in headless mode 1st use class name chromeoptions from webdriver and then define that my a object name
Chrome_options=webdriver.ChromeOptions()
Chrome_options.add_argument("headless")
Chrome_options.add_argument("--ignore-certificate-errors")

service_obj=Service("E:\chromedriver\chromedriver")
driver = webdriver.Chrome(service=service_obj ,options=Chrome_options)
driver.implicitly_wait(2)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

#to take screenshot
driver.get_screenshot_as_file("screenshot.png")