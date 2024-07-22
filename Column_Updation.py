import pandas as pd
import numpy as np

data = {
    'name': ['aj', 'shivam', 'Rohit', 'mohit'],
    'age': [28, 24, 35, 32],
    'roll': [102, 102, 103, 104],
    'marks':[11, 22, 33, 44],
    'city':['Madhubani', 'Madhubani', 'Mithila', 'Noida'],
    'gender':['F', 'M', 'M', 'F']
}
df = pd.DataFrame(data)
print("Display All Data:\n", df)

# # Update all fields of a column
# df["gender"] = "F"
# print("\nUpdate Gender Column:\n", df)


# # Update specific field of a column
# df.loc[df['roll'] == 102, 'marks'] = 999
# print("\nUpdate 'All' roll no.102  marks :\n", df)

# Replace Values
print("\n Replace 'All' Values:\n", df.replace('Madhubani', 'Delhi'))