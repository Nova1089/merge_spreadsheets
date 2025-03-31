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
dataFrameLeft = import_excel_file()
dataFrameRight = import_excel_file()
leftField = input("Specify the field in the left side spreadsheet to join on: ")
rightField = input("Specify the field on the right side spreadsheet to join on: ")
joinType = input("Specify the join type. Valid options are: left, right, outer, inner, cross: ")
# pandas.merge: https://pandas.pydata.org/docs/reference/api/pandas.merge.html
combinedFrame = pd.merge(left=dataFrameLeft, right=dataFrameRight, left_on=dataFrameLeft[leftField].str.lower(), right_on=dataFrameRight[rightField].str.lower(), how=joinType)
print("Spreadsheets have been combined")
outputName = input("Enter output file name (without the file extension): ")
timestamp = create_timestamp()
outputPath = f'.\{outputName} {timestamp}.xlsx'
print(f'Outputting to {outputPath}')
combinedFrame.to_excel(outputPath, index=False)
input("Press Enter to exit")