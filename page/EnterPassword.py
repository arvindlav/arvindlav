import time
from page.Base import BasePage
from page.HomePage import HomePage


class EnterPassword(BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def enterpassword(self):
        self.type('Password_xpath', self.prod['defaultpassword'])
        self.click('SubmitPassword_xpath')
        #time.sleep(5)
        return HomePage(self.driver)
