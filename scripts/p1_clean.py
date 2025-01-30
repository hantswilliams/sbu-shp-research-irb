import pandas as pd 

## single load of data
october2024 = pd.read_excel('data/raw/October 2024 SHP Study Update.xlsx', sheet_name='Sheet3')
december2024 = pd.read_excel('data/raw/Health Professions December Snapshot.xlsx', sheet_name='Sheet1')
january2025 = pd.read_csv('data/raw/SBU All Studies With PI And Primary Contact Info January 2025.csv')

oct24columns = october2024.columns
len(oct24columns)

dec24columns = december2024.columns
len(dec24columns)

## get list of names that are missing from dec24columns in oct24columns
missing = [col for col in oct24columns if col not in dec24columns]



