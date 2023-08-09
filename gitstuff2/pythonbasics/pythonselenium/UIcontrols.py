from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("E:\chromedriver\chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value")=="option2":
        checkbox.click()
        assert checkbox.is_selected()
        break
#driver.find_elements is used when there is dynamic change in the place of the option
#get_attribute("value")=="option2" is used to get the value of the option which should be selected
#assert is used to check result is true or false
