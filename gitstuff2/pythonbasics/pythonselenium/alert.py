from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
name="vaishu"
service_obj=Service("E:\chromedriver\chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
alertText=alert.text
print(alertText)
assert name in alertText      #this step is used to verify the text which we enter in the box appears in the alertpop0000000
alert.accept()                #it is used if we have to click ok button in alert pop,s
#alert.dismiss()              #it is used if we have to click cancel button
