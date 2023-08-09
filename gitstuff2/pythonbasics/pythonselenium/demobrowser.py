from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#-----chrome
#service_obj=Service("E:\chromedriver\chromedriver")

#webdriver.Chrome(service=service_obj)
#driver = webdriver.Chrome(service=service_obj)


#-----Firefox
#service_obj=Service("E:\geckodriver-v0.32.1-win64\geckodriver")
#driver = webdriver.Firefox(service=service_obj)


#-----Microsoft Edge
service_obj=Service("E:\edgedriver_win64\msedgedriver")
driver = webdriver.Edge(service=service_obj)

driver.get("https://staging.vshops.io/shop/63d7b3a35d7f3fd2a0815ba1")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://staging.vshops.io/shop/63d7b3a35d7f3fd2a0815ba1")
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()


