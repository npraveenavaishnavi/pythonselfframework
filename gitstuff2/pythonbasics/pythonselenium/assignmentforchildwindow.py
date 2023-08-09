from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service("E:\chromedriver\chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
#Next Module
windowsOpened=driver.window_handles
driver.switch_to.window(windowsOpened[1])

message=driver.find_element(By.CSS_SELECTOR,".im-para.red").text
var = message.split("at")[1].strip().split(" ")[0]
driver.close()
#var=driver.find_element(By.CSS_SELECTOR,"a[href='mailto:mentor@rahulshettyacademy.com']").text
#print(var)
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID,"username").send_keys("suresh")
driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("12345")
#driver.find_element(By.XPATH,"(//span[@class='checkmark'])[2]").click()
dropdown=Select(driver.find_element(By.XPATH,"//select[@class='form-control']"))
dropdown.select_by_index(0)
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".alert.alert-danger.col-md-12")))
print(driver.find_element(By.CSS_SELECTOR,".alert.alert-danger.col-md-12"))




