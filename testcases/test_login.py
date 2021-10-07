'''
Created on 25-Aug-2021

@author: SESA243476
'''
import allure

from page.HomePage import HomePage
from testresources.readingexcel import getcelldata
from testresources.readingexcel import isRunnable
import testresources.constants as constants
import pytest
from page.LandingPage import Landingpage
from page.Base import BasePage
import conftest
from conftest import objlist
import allure


@pytest.mark.usefixture("base_fixture")
class TestLogin:
    @pytest.mark.parametrize("argvals",getcelldata("LoginTest", constants.XLS_FILEPATH))
    def test_login(self,argvals):
        testrunmode = isRunnable("LoginTest", constants.XLS_FILEPATH)
        datarunmode = argvals[constants.RUNMODE]
        if testrunmode:
            if datarunmode == constants.RUNMODE_Y:
                    for i in range(0,len(objlist)):
                        pass
                    driver = objlist[i].openbrowser(argvals[constants.BROWSERNAME])
                    landingpage = Landingpage(driver)
                    login = landingpage.landingpage()
                    username = login.login()
                    password = username.enterusername()
                    homepage = password.enterpassword()
                    with allure.step("Validating Login"):
                        if(isinstance(homepage,HomePage)):
                            if(argvals['ExpectedResult']=='Success'):
                                homepage.WomenDresses()
                            else:
                                print("Home Page of the Zoho is not displayed")
                        else:
                            objlist[i].reportfailure("Login Failed")
            else:
                pytest.skip("test case is not executed due to run mode is set no no in datasheet")
        else:
            pytest.skip("test case is not executed due to run mode is set no no in testcase")