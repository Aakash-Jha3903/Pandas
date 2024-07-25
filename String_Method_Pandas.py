import pandas as pd
import numpy as np

data = {
    'name': ['aj', 'shivam', 'mohit', 'mohit'],
    'city':['Madhubani', 'Madhubani', 'Mithila', 'Noida'],
    'gender':['F', 'M', 'M', 'F']
}
df = pd.DataFrame(data)
print("Display All Data:\n", df)

"""Convert to lowercase"""
#print("\nLowercase cities:\n", df['city'].str.lower())

"""Convert to Uppercase"""
#print("\nUppercase cities:\n", df['city'].str.upper())

"""Length of String"""
#print("\nString Length cities:\n", df['city'].str.len())

"""Extract first three characters"""
#print("\nCity substrings (first 3 characters):\n", df['city'].str[:3])

"""Replace substrings"""
#print("\nCities with 'a' replaced by 'A':\n", df['city'].str.replace('a', 'A'))