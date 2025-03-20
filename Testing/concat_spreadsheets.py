import pandas as pd
import os

fp = 'C:\\Users\\MitchErekson\\Blue Raven Solar\\Fleet Management - Documents\\Dashboard\\Enterprise Billing'
dest_fp = 'C:\\Users\\MitchErekson\\Blue Raven Solar\\Fleet Management - Documents\\Dashboard\\Enterprise Billing\\Archive'
master = 'C:\\Users\\MitchErekson\\Blue Raven Solar\\Fleet Management - Documents\\Dashboard\\Master Sheets\\enterprise_master.csv'
files = os.listdir(fp)

files_xlsx = [f for f in files if f[-4:] == 'xlsx']

df = pd.DataFrame()

for f in files_xlsx: 
    data = pd.read_excel(fp + '\\' + f, 'BillingDetail_568488')
    df = pd.concat([df, data], ignore_index=True)
    d_fp = dest_fp + '\\' + f
    #os.rename(fp + '\\' + f, d_fp)
#print(df)

df.insert(0,'Vendor', 'Enterprise')

df2 = pd.read_csv(master)

df_m = pd.concat([df, df2], ignore_index=True)

df_m.to_csv(master)