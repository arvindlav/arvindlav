from page.Base import BasePage
from page.SummerDresses import SummerDresses


class Dresses(BasePage):
    def __init__(self,driver):
        super().__init__()
        self.driver = driver

    def Dresses(self):
        self.click('Dresses_xpath')
        return SummerDresses(self.driver)