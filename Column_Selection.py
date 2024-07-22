import pandas as pd
import numpy as np

data = {
    'name':['Aakash','Shivam','Ajay','Ajay','Rohan','Mohan',np.nan ],
    'age':[ 24,20,22,np.nan,21,np.nan,20 ],
    'City': ['Noida', 'Delhi', 'Mumbai', 'Pune','Goa','Patna','Lucknow']
    }


df = pd.DataFrame(data)

# print("Display all Data : \n",df)
# print("\nSingle Column Data : \n",df["age"])
# print("\n Sum of Single Column Data : \n",df["age"].sum())

# print("\n Empty DataFrame : \n",df[[]])
# print("\nMultiple Column Data : \n",df[["age" , "name","City"]])
## print("\n Empty DataFrame : \n",df[])

# print("\nSelect Row by integer Location : \n",df.iloc[2])
# print("\nSelect Row by Label : \n",df.loc[2])

print("\nSlice Row : \n",df[2:5])
print("\nSelect Rows by Condition(T/F) : \n",df["age"]>20)
print("\nSelect Rows by Condition : \n",df[df["age"]>20])


