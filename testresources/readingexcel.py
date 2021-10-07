'''
Created on 24-Aug-2021

@author: SESA243476
'''
from testresources.readdata import XLSReader
import testresources.constants as constants

def getcelldata(testcasename,path):
    datalist = []
    #testcasename = "TestA"
    xls = XLSReader(path)
    #print(xls.getCellData("Datasheet", 0, 0))
    
    testrowindex = 0

    
    while not(xls.getCellData(constants.DATASHEET,testrowindex,0)==testcasename):
        testrowindex =testrowindex + 1
    
    colstartrowindex = testrowindex + 1
    datastartrowindex = colstartrowindex + 1
    
    maxrow = 0
    try:
        while not(xls.checkemptycell(constants.DATASHEET, datastartrowindex + maxrow, 0)):
            maxrow = maxrow+1
    except Exception:
        print(Exception)
        
    maxcol = 0
    try:
        while not(xls.checkemptycell(constants.DATASHEET, colstartrowindex, maxcol)):
            maxcol = maxcol + 1
    except Exception:
        print(Exception)
        #print(maxcol)
    
    for rNum in range(datastartrowindex,datastartrowindex+maxrow):
        datadictionary = {}
        for cNum in range(0,maxcol):
            datakey = xls.getCellData(constants.DATASHEET,colstartrowindex,cNum)
            datavalue = xls.getCellData(constants.DATASHEET,rNum,cNum) 
            #print(datakey + "------"+datavalue)
            datadictionary[datakey] = datavalue
            #print(datadictionary)
        datalist.append(datadictionary)
    return datalist  
#getcelldata()
def isRunnable(testcasename,path):
    #testcasename = "TestA"
    xls = XLSReader(path)
    rows = xls.getrowcount(constants.TESTSHEET)
    #print(rows)
    for nrows in range(0,rows):
        tname = xls.getCellDatabyColname(constants.TESTSHEET,nrows,constants.TCID)
        if (tname == testcasename):
            runmode = xls.getCellDatabyColname(constants.TESTSHEET,nrows,constants.RUNMODE)
            #print(runmode)
            if(runmode==constants.RUNMODE_Y):
                return True
            else:
                return False
#isRunnable()