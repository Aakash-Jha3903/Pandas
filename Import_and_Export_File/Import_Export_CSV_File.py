# Import Export CSV File
import pandas as pd
import numpy as np

data = {
    'name': ['aj', 'shivam', 'mohit', 'mohit'],
    'city': ['Madhubani', 'Madhubani', 'Mithila', 'Noida'],
    'age': [28, 24, 24, np.nan],
}
df = pd.DataFrame(data)
# Writing DataFrame to CSV file
df.to_csv('Import_and_Export_File/sample.csv', index=False)  # Without index

# Reading the CSV file back into a DataFrame
df_read = pd.read_csv('Import_and_Export_File/sample.csv')
print(df_read)
