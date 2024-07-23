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


""" Calculate the mean of the 'age' column"""
#age_mean = df['age'].mean()
#print("\nMean age:", age_mean)

""" Calculate the mean of the 'age' column including NaN values"""
#age_mean_with_nan = df['age'].mean(skipna=False)
#print("\nMean age including NaN:", age_mean_with_nan)

""" Calculate the mean of 'age' and 'marks' columns"""
#selected_means = df[['age', 'marks']].mean()
#print("\nAge and Marks Mean:\n", selected_means)

""" Apply a single aggregation function"""
#age_mean = df['age'].agg('mean')
#print("\nMean age:", age_mean)

""" Apply multiple aggregation functions"""
#age_stats = df['age'].agg(['mean', 'min', 'max'])
#print("\nAge statistics:\n", age_stats)

""" Apply different aggregation functions to different columns"""
custom_agg = df.agg({
    'age': ['mean', 'min', 'max'],
    'marks': 'sum',
    'roll': 'count'
})
print("\nCustom aggregation:\n", custom_agg)