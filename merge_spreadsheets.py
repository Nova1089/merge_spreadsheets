import pandas as pd
import os.path
from datetime import datetime
from pandas.io.formats import excel

# functions
def show_intro():
    print("This script combines excel files.")
    input("Press Enter to continue: ")

def set_output_format():
    excel.ExcelFormatter.header_style = None

def import_excel_file():
    keep_going = True
    while keep_going:        
        path = input("Enter path to excel file: ")
        path = path.strip('"')
        file_exists = os.path.isfile(path)
        if not(file_exists):
            print("File not found. Please try again.")
            keep_going = True
        else:
            keep_going = False
    return pd.read_excel(path)

def create_timestamp():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d-%H-%M")
    return timestamp

# main
show_intro()
set_output_format()
data_frame_1 = import_excel_file()
data_frame_2 = import_excel_file()
combined_frame = pd.merge(data_frame_1, data_frame_2, on='VIN', how='outer')
timestamp = create_timestamp()
output_path = f'C:\\Users\\Zak\\Desktop\\IT Labs\\Scripts\\Python\\Spreadsheet Merge Project\\mock simple outer {timestamp}.xlsx'
print(f'Outputting to {output_path}')
combined_frame.to_excel(output_path, index=False)
input("Press Enter to exit")