import pandas as pd
import numpy as np

data = {
    'name': ['aj', 'shivam', 'mohit', 'mohit'],
    'city':['Madhubani', 'Madhubani', 'Mithila', 'Noida'],
    'age': [28, 24, 35, 32, 28, 24, np.nan, 32, 28, 24],
}

df = pd.DataFrame(data)
print("Display All Data:\n", df)

# Function to convert names to uppercase
def to_uppercase(name):
    return name.upper()

# Apply the to_uppercase function to the 'name' column using map()
df['name'] = df['name'].map(to_uppercase)

# Display the modified DataFrame
print("\nDataFrame after applying map() to 'name' column:")
print(df)