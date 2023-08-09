from selenium.webdriver.common.by import By

from pageObject.confirmpage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']
    # #productName = product.find_element(By.XPATH, "div/h4/a").text
    products = (By.XPATH, "//div[@class='card h-100']//div/h4/a")

    #productname = products.__contains__("Blackberry")
        #(By.XPATH.count("Blackberry"))
    productname = (By.XPATH, "//a[normalize-space()='Nokia Edge']")
    # product.find_element(By.XPATH, "div/button").click()
    addbutton = (By.XPATH, "//app-card[3]//div[1]//div[2]//button[1]")
    #addbutton = (By.XPATH, "//button[@class='btn btn-info'][normalize-space()='Add'])[4]")

    def getproductsTitles(self):
        return self.driver.find_elements(*CheckOutPage.products)

    def getproductName(self):
        return self.driver.find_element(*CheckOutPage.productname)

    def getaddButton(self):
        return self.driver.find_element(*CheckOutPage.addbutton)
