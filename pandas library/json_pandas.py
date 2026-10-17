import pandas as pd
df=pd.read_json("data.json")
print(df.to_string())           # to string print entire data frame from the file 



print(df.head(10))   #to print top 10 data
print(df.tail(10))      # to print last 10 data from the file of the data list 


print(df.info())        # to gives you more information about the data set 
