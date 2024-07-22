import pandas as pd


# Create a dictionary of data
data = {'Name': ['Aakash', 'Shivam', 'Rudra', 'Sona'],
        'Age': [24, 23, 22, 23],
        'City': ['Noida', 'Delhi', 'Mumbai', 'Pune']}

# Create a DataFrame
df = pd.DataFrame(data)
df = pd.DataFrame(data, index=[i for i in range(1, 5)])

# print(df)
# print("Index of df are :\n",df.index)
# print("names of df are :\n",df.Name)


# print("city of df are :\n",df.City.get(1))  """get() take the index value """
print("\nage of df are :\n", df.Age)
print("\nage[ using get('Age') ] of df are :\n", df.get("Age"))
print("\nage[ using get(index-key) ] of df are :\n", df.Age.get(1))
