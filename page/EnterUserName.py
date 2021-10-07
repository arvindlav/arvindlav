'''
Created on 22-Aug-2021

@author: SESA243476
'''
import time
from page.Base import BasePage
from page.EnterPassword import EnterPassword


class Enterusername(BasePage):
    def __init__(self,driver):
        super().__init__()
        self.driver = driver
        
    def enterusername(self):
        self.type('Username_xpath',self.prod['defaultusername'])
        #self.click('SubmitEmail_xpath')
        return EnterPassword(self.driver)