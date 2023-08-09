from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj=Service("E:\geckodriver-v0.32.1-win64\geckodriver")
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am using frames")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME,"h3").text)