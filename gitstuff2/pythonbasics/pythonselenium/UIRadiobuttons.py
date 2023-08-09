from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("E:\chromedriver\chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#buttons =driver.find_elements(By.XPATH,"//input[@type='radio']")
#print(len(buttons))
#for radio in buttons:
    #if radio.get_attribute("value")=="radio2":
        #radio.click()
        #assert radio.is_selected()
        #break
#another method of selecting the radio button if we exactly know the positions of value then directly use the index[]

radiobuttons =driver.find_elements(By.CSS_SELECTOR,".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

#is_displayed() method is used if the option is displayed on screen or not
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()