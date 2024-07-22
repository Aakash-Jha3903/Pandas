import pandas as pd


data = {
    "Department": ["IT", "Finance", "IT"],
    "Job Title": ["Software Engineer", "Senior Software Engineer", "Project Manager"],
    "Salary": pd.Series([50000, 60000]),
    "Room No.": pd.Series([i for i in range(20, 26, 2)]),
}
df = pd.DataFrame(data)
# print(df)


"""index ki value match hona chachie"""
data2 = {
    "Salary": pd.Series([40000, 50000], index=["aa", "bb"]),
    "Room No.": pd.Series([i for i in range(15, 19)], index=["aa", "bb", "cc", "dd"]),
}
df2 = pd.DataFrame(data2, index=[i for i in range(1, 4)])
df2 = pd.DataFrame(data2)
df2 = pd.DataFrame(data2, index=["aa", "bb", "cc", "dd", "ee", "ff"])
# print(df2)

data3 = [
    {"a": 1, "b": 2,"c": 3},
    {"a": 10, "b": 20, "c": 30, "d": 40},
]
df3 = pd.DataFrame(data3)
print(df3)