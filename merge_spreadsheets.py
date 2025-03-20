import pandas as pd
import os.path
from datetime import datetime
from pandas.io.formats import excel
excel.ExcelFormatter.header_style = None

# functions
def show_intro():
    print("This script combines excel files.")
    input("Press Enter to continue: ")

def import_excel_file():
    keepGoing = True
    while keepGoing:        
        path = input("Enter path to excel file: ")
        path = path.strip('"')
        fileExists = os.path.isfile(path)
        if not(fileExists):
            print("File not found. Please try again.")
            keepGoing = True
        else:
            keepGoing = False
    return pd.read_excel(path)

def create_timestamp():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d-%H-%M")
    return timestamp

# main
show_intro()
dataFrame1 = import_excel_file()
dataFrame2 = import_excel_file()
leftField = input("Specify the field in the left spreadsheet to join on: ")
rightField = input("Specify the field on the right spreadsheet to join on: ")
joinType = input("Specify the join type. Valid options are: left, right, outer, inner, cross: ")
# pandas.merge: https://pandas.pydata.org/docs/reference/api/pandas.merge.html
combinedFrame = pd.merge(left=dataFrame1, right=dataFrame2, left_on=leftField, right_on=rightField, how=joinType)
print("Spreadsheets have been combined")
outputName = input("Enter output file name (without the file extension): ")
timestamp = create_timestamp()
outputPath = f'.\{outputName} {timestamp}.xlsx'
print(f'Outputting to {outputPath}')
combinedFrame.to_excel(outputPath, index=False)
input("Press Enter to exit")