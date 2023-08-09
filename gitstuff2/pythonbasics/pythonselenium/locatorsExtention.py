from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service

#----chrome
from selenium.webdriver.common.by import By


service_obj=Service("E:\chromedriver\chromedriver")

#webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client/")
#here we are using "linkText" locator
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
#we can travel from parent class to child class Eg:for XPATH--//form/div[index line num]/input
                                                   #for CSS---form div:nth-child(index line num)input

driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("vaishu@123")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("vaishu@123")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
#another way of writing xpath for button Save New Password
#driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()

