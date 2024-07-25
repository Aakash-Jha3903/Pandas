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
print("Display All Data:\n", df)

"""Use value_counts to count unique values in the 'city' column"""
city_counts = df['city'].value_counts()
print("\nCity counts:\n", city_counts)

"""Use value_counts to count unique values in the 'name' column"""
name_counts = df['name'].value_counts()
print("\nName counts:\n", name_counts)

"""Use value_counts to count unique values in the 'age' column including NaN values"""
age_counts = df['age'].value_counts(dropna=False)
print("\nAge counts including NaN:\n", age_counts)

"""Use value_counts with sorting by index"""
city_counts_sorted = df['city'].value_counts().sort_index()
print("\nCity counts sorted by index:\n", city_counts_sorted)