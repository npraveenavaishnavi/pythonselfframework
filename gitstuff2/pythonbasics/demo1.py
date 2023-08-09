from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#class Test:
    #def test_form(self):
service_obj=Service("E:\chromedriver\chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("vaishu")
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
driver.find_element(By.XPATH,"//input[@value='Submit']").click()
alertText=driver.find_element(By.CLASS_NAME, "alert-success").text
assert ("success"in alertText)
driver.close()


