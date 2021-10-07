'''
Created on 23-Aug-2021

@author: SESA243476
'''
import xlrd

class XLSReader():
    def __init__(self,path):
        self.path = path
        self.readxls = xlrd.open_workbook(self.path)
    
    def getCellData(self,sheetname,rowindex,colindex):
        sheet = self.readxls.sheet_by_name(sheetname)
        return sheet.cell_value(rowindex,colindex)
    
    def getCellDatabyColname(self,sheetname,rowindex,colname):
        try:
            sheet = self.readxls.sheet_by_name(sheetname)
        except Exception:
            print(Exception)
        for cnum in range(0,self.getcoloumncount(sheetname)):
            extractedcolname = sheet.cell_value(0,cnum)
            if(extractedcolname==colname):
                celldata = sheet.cell_value(rowindex,cnum)
                if celldata != '':
                    return celldata
                else:
                    return ''
            
    
    def checkemptycell(self,sheetname,rowindex,colindex):
        sheet = self.readxls.sheet_by_name(sheetname)
        celltype = sheet.cell_type(rowindex,colindex)
        #$print(celltype)
        if(celltype==xlrd.XL_CELL_EMPTY):
            return True
        else:
            return False
    
    def getrowcount(self,sheetname):
        sheet = self.readxls.sheet_by_name(sheetname)
        return sheet.nrows
        
    def getcoloumncount(self,sheetname):
        sheet = self.readxls.sheet_by_name(sheetname)
        return sheet.ncols
        