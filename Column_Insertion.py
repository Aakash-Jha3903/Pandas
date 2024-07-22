import pandas as pd
import numpy as np

data = {
    'name':['Aakash','Shivam','Ajay','Ajay','Rohan','Mohan',np.nan ],
    'age':[ 24,20,22,np.nan,21,np.nan,20 ],
    'City': ['Noida', 'Delhi', 'Mumbai', 'Pune','Goa','Patna','Lucknow']
    }


df = pd.DataFrame(data)
# print("Display all Data : \n",df)

# df["Result"] = "pass"
# print("After Insertion of Column at the End : \n",df)

# df["marks"] = [95,98,69,96,56,85,33]
# print("After Insertion of Array Marks-Column : \n",df)

# """insert() - It is used to insert column at particular location """
# hobbies = ["Football", "Cricket", "reading", "singing", "chatting", "computer", "fighting",]
# df.insert(2, "hobbies", hobbies)
# print("Insert Column at index 2 :\n", df)
          
"""Calculate Column to create New Column """
df["fees"] = df["age"] * 12
print("\n Fees Column Added:\n", df)







