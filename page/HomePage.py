from page.Add_Cart import AddCart
from page.Base import BasePage
from page.Dresses import Dresses


class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__()
        self.driver = driver

    def WomenDresses(self):
        self.logging("I am in Home Page")
        self.click('WomenDresses_xpath')
        return Dresses(self.driver)

