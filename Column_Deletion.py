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

"""Delete single Column"""
#del df['gender']
#print("\nGender Column Deleted:\n", df)

"""Pop single column """
# print("\nPOP City:\n", df.pop('city'))
# print("\nData after POP City:\n", df)
##print("\nTypeError: DataFrame.pop() missing 1 required positional argument: 'item' \n", df.pop())

"""Delete Multiple column drop() which returns the data after deletion
            { DOESN'T CHANGE THE REAR DATA } """
# newdf = df.drop(columns=['name', 'roll'])
# print("\nDrop Name and Roll:\n", newdf)
# print("\n Data:\n", df)

""" Delete Duplicate Values { DOESN'T CHANGE THE REAR DATA } """
#print("\n Delete Duplicates:\n", df.drop_duplicates('name'))