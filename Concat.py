import pandas as pd

# Create DataFrames
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

df2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7']
})

df3 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

"""Vertical Concatenation"""
vertical_concat = pd.concat([df1, df2])
print("Vertical Concatenation:\n", vertical_concat)

"""Horizontal Concatenation"""
horizontal_concat = pd.concat([df1, df2], axis=1)
print("\nHorizontal Concatenation:\n", horizontal_concat)

"""Concatenation with Different Columns"""
different_columns_concat = pd.concat([df1, df3], axis=1)
print("\nConcatenation with Different Columns:\n", different_columns_concat)