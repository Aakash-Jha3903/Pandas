import pandas as pd
print("Namaste Pandas \n")

a = pd.Series([10, 20, 30, 40, 50])
b = pd.Series([10, 20, 30, 40, 50],index=["a","a","c","d","e"])
c = pd.Series({"a":1,"b":2,"c":3 })

d = pd.Series(5.0,index=["a","a","c","d","e"])



print(d)
print(d.dtype)  # float64
print(d.index)  # Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
print(d.values) # [5. 5. 5. 5. 5.]

print(d.keys)   # same as "d"
print("GET valueS : ",b.get("a")) 