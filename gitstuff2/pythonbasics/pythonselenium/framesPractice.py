from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj = Service("E:\geckodriver-v0.32.1-win64\geckodriver")
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,1500);")
driver.switch_to.frame("iframe-name")
driver.find_element(By.CSS_SELECTOR, ".nav-outer.clearfix >nav > div:nth-child(2) > ul > li:nth-child(4)").click()
#driver.implicitly_wait(60)
# windowsOpened=driver.window_handles
# driver.switch_to.window(windowsOpened[1])
print("hello")
print(driver.find_element(By.CSS_SELECTOR, ".inner-box h1").text)
assert driver.find_element(By.CSS_SELECTOR, ".inner-box h1").text == "LEARNING PATHS"
driver.close()
