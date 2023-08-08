from openpyxl import load_workbook
import pandas as pd

filename = 'Attendance System.xlsx'

# name = str(input('Enter name: '))
# print('Name is: ' + name)

workbook = load_workbook(filename=filename)
sheet_num = len(workbook.sheetnames)

sheet1 = pd.read_excel(filename, sheet_name=None, index_col=0)
sheets = pd.concat(sheet1.values())
print(sheets)


