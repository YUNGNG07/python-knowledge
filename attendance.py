from openpyxl import load_workbook
import pandas as pd
import numpy as np
import datetime

filename = 'Attendance System.xlsx'
now = datetime.datetime.now().strftime('%d-%b-%Y %H:%M:%S')

def read(name):
    # Read all Excel data from multiple sheets into one DataFrame
    sheets = pd.concat(pd.read_excel(filename, sheet_name=None), ignore_index=True)

    # Check through every name
    for names in sheets['Name']:
        # print(names)
        sheets = sheets.replace(np.nan, '')
        if name == names:
            print('Found ' + name)
            # Select rows from a DataFrame based on column values
            details = sheets.loc[sheets['Name'] == name]
            sheets.at[int(details.index.values), 'Attendance'] = 'Yes'
            sheets.at[int(details.index.values), 'Timestamp'] = now
            sheets.to_excel('Output.xlsx')
        else:
            continue
            # print('This person is not in this department')

    print(sheets)

if __name__ == '__main__':
    while True:
        name = str(input('Enter name: '))
        # name = 'J'
        read(name)
