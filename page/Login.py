'''
Created on 22-Aug-2021

@author: SESA243476
'''
from page.EnterUserName import Enterusername
from page.Base import BasePage

class Login(BasePage):
    
    def __init__(self,driver):
        super().__init__()
        self.driver = driver
        
    def login(self):
        self.click('Login_xpath')
        return Enterusername(self.driver)