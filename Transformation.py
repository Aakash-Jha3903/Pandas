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

""" Apply a single transformation function """
#age_plus_one = df['age'].transform(lambda x: x + 1)
#print("\nAge plus one:\n", age_plus_one)

""" Apply a built-in transformation function to a Series """
#age_squared = df['age'].transform(np.sqrt)
#print("\nAge squared:\n", age_squared)

""" Apply a single transformation function to multiple columns """
#df_transformed = df[['age', 'marks']].transform(lambda x: x * 2)
#print("\nDataFrame transformed (age and marks doubled):\n", df_transformed)

""" Apply different transformation functions to different columns """
df_transformed_diff = df.transform({
    'age': lambda x: x + 10,
    'marks': lambda x: x - 10
})
print("\nDataFrame transformed with different functions:\n", df_transformed_diff)