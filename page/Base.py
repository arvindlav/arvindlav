'''
Created on 22-Aug-2021

@author: SESA243476
'''
import logging

import conftest
import testresources.constants as constants
import selenium.webdriver
from _overlapped import NULL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
global driver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure
from _datetime import datetime
from allure_commons.types import AttachmentType
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.webdriver import WebDriver

class BasePage():
    def __init__(self):
        self.driver = NULL
        self.prod = conftest.prod
        self.logger = logging.getLogger()
              
    #common utility function
    def take_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(),"Screenshot at:" + str(datetime.now()),AttachmentType.PNG)
    def waitforpageloaded(self):
        i=1
        while(i!=10):
            load_status = self.driver.execute_script("return document.readystate")
            if(load_status=='complete'):
                break
            else:
                time.sleep
    
    def iselementpresent(self,obj):
        wait = WebDriverWait(self.driver,20)
        element = self.prod[obj]
        #self.waitforpageloaded()
        if(obj.endswith('_xpath')):
            elementlist = wait.until(EC.presence_of_element_located((By.XPATH,element)))
        elif(obj.endswith('_id')):
            elementlist = wait.until(EC.presence_of_element_located((By.ID,element)))
        elif(obj.endswith('_classname')):
            elementlist = wait.until(EC.presence_of_element_located((By.CLASS_NAME,element)))
        elif(obj.endswith('_tagname')):
            elementlist = wait.until(EC.presence_of_element_located((By.TAG_NAME,element)))
        elif(obj.endswith('_css')):
            elementlist = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,element)))
        else:
            elementlist = wait.until(EC.presence_of_element_located((By.LINK_TEXT,element)))
        if  (elementlist!=None):
            return True
        else:
            return False
        
    def iselementvisibilty(self,obj):
        wait = WebDriverWait(self.driver,20)
        element = self.prod[obj]
        #self.waitforpageloaded()
        if(obj.endswith('_xpath')):
            elementlist = wait.until(EC.visibility_of_all_elements_located((By.XPATH,element)))
        elif(obj.endswith('_id')):
            elementlist = wait.until(EC.visibility_of_all_elements_located((By.ID,element)))
        elif(obj.endswith('_classname')):
            elementlist = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME,element)))
        elif(obj.endswith('_tagname')):
            elementlist = wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME,element)))
        elif(obj.endswith('_css')):
            elementlist = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,element)))
        else:
            elementlist = wait.until(EC.visibility_of_all_elements_located((By.LINK_TEXT,element)))
        if (elementlist!=None):
            return True
        else:
            return False
        
    def getelement(self,locator):
        obj = self.prod[locator]
        if(self.iselementpresent(locator) and self.iselementvisibilty(locator)):
            try:
                if(locator.endswith('_xpath')):
                    element = self.driver.find_element_by_xpath(obj)
                elif(locator.endswith('_id')):
                    element = self.driver.find_element_by_id(obj)
                elif(locator.endswith('_classname')):
                    element = self.driver.find_element_by_name(obj)
                elif(locator.endswith('_tagname')):
                    element = self.driver.find_element_by_tagname(obj)
                elif(locator.endswith('_css')):
                    element = self.driver.find_element_by_css_selector(obj)
                elif(locator.endswith('_linktext')):
                    element = self.driver.find_element_by_linktext(obj)
                else:
                    return False
                return element
            except Exception:
                print("Element not Found" + Exception)        
        else:
            print("Element is not either found or visible")
            
    def openbrowser(self,browser):
        with allure.step("Opening "+  browser):
            if(browser==constants.CHROME):
                self.driver = webdriver.Chrome(ChromeDriverManager().install())
            elif(browser==constants.FIREFOX):
                self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            elif(browser==constants.EDGE):
                self.driver = webdriver.Edge(r"msedgedriver.exe")
                print("edge luanched")
            else:
                self.driver = webdriver.Ie()
            self.take_screenshot()
            return self.driver

    def navigate(self):      
        url= self.prod['URL'] 
        with allure.step("Navigating to " +url):
            self.driver.get(url)
            self.take_screenshot()
    
    def click(self,object_click):
        with allure.step("Clicking on " + object_click):
            self.getelement(object_click).click()
            self.take_screenshot()
    
    def type(self,object_type,data):
        with allure.step("Typing on " + object_type + " with " + data):
            self.getelement(object_type).send_keys(data)
            self.take_screenshot()
    
    def quit(self):
        if(self.driver!=NULL):
            self.driver.quit()

    def logging(self,message):
        self.logger.setLevel(logging.INFO)
        self.logger.info(message)

    def reportfailure(self,message):
        self.take_screenshot()
        assert False, message

    def reportsuccess(self,message):
        self.logging(message)
        assert True

    #Validate Functions
    def validatetitle(self):
        expectedtitle = self.prod['expectedhomepagetitle']
        actualtitle = self.driver.title
        if expectedtitle == actualtitle:
            self.reportsuccess("Title Validation Successful")
            #report Success
        else:
            self.logging("Title Validation Failed.Got Title as " + actualtitle + " instead of " + expectedtitle)
            # report Failure


