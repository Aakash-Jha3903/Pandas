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

"""  isin([....])  """
dt1 = df['age'].isin([28, 32])
print(dt1)

dt2 = df[df['age'].isin([28, 32])]
print(dt2)