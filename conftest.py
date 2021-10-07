'''
Created on 22-Aug-2021

@author: SESA243476
'''
from pyjavaproperties import Properties
import testresources.constants as constants
import pytest
from page.Base import BasePage
import allure

prod = Properties()
#set up and tear down-fxture
objlist = []
@pytest.yield_fixture(scope ='function', autouse=True)
def base_fixture():
    with allure.step("Initializing block...."):
        try:
            prodpath = open(constants.ENVIRONMENT_PROPERTIES)
            prod.load(prodpath)
            #prod.list()
            base = BasePage()
            objlist.append(base)
        except Exception:
            pass
    
    yield locals()
    with allure.step("Finishing up...."):
        base.quit()
        