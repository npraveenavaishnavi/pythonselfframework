
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

service_obj=Service("E:\chromedriver\chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action=ActionChains(driver)
#action.click_and_hold(driver.find_elements(By.))
#action.double_click()
#action.context_click()    used to right click
#action.move_to_element()
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()