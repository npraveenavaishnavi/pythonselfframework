from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
browserSortedVeggies=[]
service_obj=Service("E:\chromedriver\chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#click on the header
#collect all veggiesname->BrowserSortedList(A,B,C)
#sort this BrowserSortedList=NewSortedList(A,B,C)

#click on the header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
#collect all veggiesname->BrowserSortedList(A,B,C)
veggieWebElements=driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList=browserSortedVeggies.copy()

#sort this BrowserSortedList=NewSortedList(A,B,C)
browserSortedVeggies.sort()
assert browserSortedVeggies==originalBrowserSortedList
