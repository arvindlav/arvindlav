'''
Created on 22-Aug-2021

@author: SESA243476
'''
from page.Login import Login
from page.Base import BasePage

class   Landingpage(BasePage):
    
    def __init__(self,driver):
        super().__init__()
        self.driver = driver
        
    def landingpage(self):
        self.navigate()
        self.validatetitle()
        return Login(self.driver)