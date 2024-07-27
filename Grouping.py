import pandas as pd


data = {
    'team': ['A', 'A', 'B', 'B', 'C', 'C'],
    'player': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'points': [10, 15, 10, 20, 10, 25]
}
df = pd.DataFrame(data)

""" Display the DataFrame"""
print("Original DataFrame:\n", df)

""" Group by 'team' and calculate the sum of 'points'"""
grouped_sum = df.groupby('team').sum()
print("\nGrouped by Team and summed:\n", grouped_sum)

""" Group by 'Team' and 'Player' and calculate the sum of 'Points'"""
grouped_multi = df.groupby(['team', 'player']).sum()
print("\nGrouped by Team and Player and summed:\n", grouped_multi)

""" Group by 'Team' and calculate various aggregations"""
grouped_agg = df.groupby('team').agg({
    'points': ['sum', 'mean', 'max']
})
print("\nGrouped by Team with multiple aggregations:\n", grouped_agg)

""" Calculate the mean Points by Team and assign it to each row """
df['meanpoints'] = df.groupby('team')['points'].transform('mean')
print("\nMean Points by Team assigned to each row:\n", df)

""" Iterate over groups """
for name, group in df.groupby('team'):
    print(f"\nGroup: {name}")
    print(group)