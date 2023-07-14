from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):  # this step is called as creating a constructor
        self.driver = driver

    # self.driver.find_element(By.CSS_SELECTOR, " a[href*='shop']").click()
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email= (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender= (By.ID,"exampleFormControlSelect1")
    submit= (By.XPATH,"//input[@value='Submit']")
    successmsg= (By.CLASS_NAME,"alert-success")



    # shop is referred as object created for class homepage
    def shopitems(self):
        return self.driver.find_element(*HomePage.shop)  # this step is called call the class variable inside the method as class name.objectname

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessmsg(self):
        return self.driver.find_element(*HomePage.successmsg)



