import pandas as pd


data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'City': ['Bokaro', 'Ranchi', 'Dhanbad', 'Dumka'],
    'Sales': [200, 150, 300, 200],
    'Expenses': [50, 60, 70, 80]
}
df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

# Basic Pivot Table
pivot = pd.pivot_table(df, values='Sales', index='Date',
                       columns='City', aggfunc='sum')
print("\nPivot Table:\n", pivot)

# Multiple Aggregation Functions
pivot_multi = pd.pivot_table(df, values=['Sales', 'Expenses'], index='Date', columns='City',
                             aggfunc={'Sales': 'sum', 'Expenses': 'mean'})
print("\nPivot Table with Multiple Aggregations:\n", pivot_multi)

# Adding Margins (Subtotals)
pivot_margins = pd.pivot_table(df, values='Sales', index='Date', columns='City',
                               aggfunc='sum', margins=True)
print("\nPivot Table with Margins:\n", pivot_margins)

# Filling Missing Values
pivot_fill = pd.pivot_table(df, values='Sales', index='Date', columns='City',
                            aggfunc='sum', fill_value=0)
print("\nPivot Table with Fill Value:\n", pivot_fill)
