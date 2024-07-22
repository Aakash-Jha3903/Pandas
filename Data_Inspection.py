import pandas as pd
import numpy as np

data = {
    'name':['Aakash','Shivam','Ajay','Ajay','Rohan','Mohan',np.nan ],
    'age':[ 24,20,22,np.nan,21,np.nan,20 ]
}

df = pd.DataFrame(data)
# print(df)

# print("Info :\n", df.info)
# print("null Info :\n", df.isnull())
# print("total null Info :\n", df.isnull().sum())

# print("Statistical summary : ",df.describe())

# print("Top 5 data : ",df.head())
# print("Top 10 data : ",df.head(10))
# print("Bottom 5 data : ",df.tail())
# print("Bottom 10 data : ",df.tail(10))

# print("Duplicated names :\n",df["name"].duplicated())
# print(" Total Duplicated in age : ",df["age"].duplicated().sum())

# print("Sort by index : ",df.sort_index())
# print("\nSort by value : \n",df.sort_values("age"))



