import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedResult=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actualResult=[]
service_obj=Service("E:\chromedriver\chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)
#5 sec is max time out(if it oly 2 sec then it saves 3 sec)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(results)

assert count > 0
for result in results:
    actualResult.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()
assert expectedResult==actualResult

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#SUM validation
prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum=0
for price in prices:
    sum=sum+int(price.text)
print(sum)

totalamount=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum==totalamount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))

print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
discountedAmt= float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert totalamount > discountedAmt
