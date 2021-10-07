#from . import Add_Cart
from page.Base import BasePage
#from page.Add_Cart import AddCart
#from .Add_Cart import AddCart


class SummerDresses(BasePage):
    def __init__(self,driver):
        super().__init__()
        self.driver = driver

    def SelectDress(self,item):
        self.click('SummerDresses_xpath')
        itemselection = item.split(',')
        length = len(itemselection)
        for selitem in itemselection:
           if selitem == "Printed Chiffon Dress":
               self.addcart('PrintedChiffonDress_xpath')
           else:
                self.addcart('PrintedSummerDress_xpath')

    def addcart(self,obj_click):
        self.click(obj_click)
        self.click('ADDCart_xpath')
        self.click('layercart_xpath')
        self.driver.back()