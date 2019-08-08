import openpyxl

wk = openpyxl.Workbook()
sh = wk.active
sh.title = "Test"

print(sh.title)

sh['A3'].value="test.com"

#2nd Sheet is Created
wk.create_sheet(title="TestingW")
sh1 = wk['TestingW']
sh1['A6']='9876543210'

#Saving
wk.save("C:\\Users\\minds9\\Documents\\Book1.xlsx")
