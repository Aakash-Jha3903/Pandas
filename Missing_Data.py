import pandas as pd
import numpy as np

data = {
    'name': ['aj', 'shivam', 'mohit', 'mohit'],
    'age': [28, 24, 35, 32],
    'roll': [102, 102, 103, 104],
    'marks':[11, 22, 33, 44],
    'city':['Madhubani', 'Madhubani', 'Mithila', 'Noida'],
    'gender':['F', 'M', 'M', 'F']
}
df = pd.DataFrame(data)
# print("Display All Data:\n", df)

"""Boolean Mask where values are nan"""
#print(df.isna())
#print(df.isna().sum())

""" Fill some Value in Missing Data """
#print(df.fillna(value=123))

""" Drop missing data """
#print(df.dropna())

""" Backward Filling """
#print(df.bfill())

""" Forward Filling """
#print(df.ffill())