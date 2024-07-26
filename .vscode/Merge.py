import pandas as pd

""" Create DataFrames""" 
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Sonam', 'Raj', 'Sonal', 'Rajeev']
})

df2 = pd.DataFrame({
    'id': [3, 4, 5, 6],
    'score': [90, 80, 70, 60]
})

""" Inner Join""" 
inner_join = pd.merge(df1, df2, on='id')
print("Inner Join:\n", inner_join)

""" Left Join""" 
left_join = pd.merge(df1, df2, on='id', how='left')
print("\nLeft Join:\n", left_join)

""" Right Join""" 
right_join = pd.merge(df1, df2, on='id', how='right')
print("\nRight Join:\n", right_join)

""" Outer Join""" 
outer_join = pd.merge(df1, df2, on='id', how='outer')
print("\nOuter Join:\n", outer_join)

df3 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Sonam', 'Raj', 'Sonal', 'Rajeev']
})

df4 = pd.DataFrame({
    'stu_id': [3, 4, 5, 6],
    'score': [90, 80, 70, 60]
})
""" Inner Join""" 
inner_join = pd.merge(df3, df4, left_on='id', right_on='stu_id')
print("Inner Join:\n", inner_join)
