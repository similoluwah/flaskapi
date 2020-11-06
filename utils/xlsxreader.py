import pandas as pd 

def readXLSX(filepath):
    result = pd.read_excel(filepath)
    return [{"phone_number" : rows.phone_number, "run_time" : rows.run_time} for index, rows in result.iterrows()]