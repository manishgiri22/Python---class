import pandas as pd 
titanic=pd.read_csv("data/titanic.csv")     # pandas provides the read_csv() function to read data stored in csv 
# first and last 5 row data will shown by default 
print(titanic.head(8))  # print the first 8 rows of the data
print(titanic.tail(8))  # print the last 8 rows of the data
pd.dtypes(titanic)
 