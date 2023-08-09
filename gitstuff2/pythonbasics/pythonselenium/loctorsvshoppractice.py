from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service

#----chrome
from selenium.webdriver.common.by import By

service_obj=Service("E:\chromedriver\chromedriver")

#webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome(service=service_obj)
driver.get("https://staging.vshops.io/admin")
driver.find_element(By.CSS_SELECTOR,"#Username").send_keys("freshgroceries")
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("Vaishnavi12")
driver.find_element(By.XPATH,"//button[@type='submit']").click()