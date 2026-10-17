import pandas as pd
mydataset={
   'liss':["manish",'giri','lalit'],        #dictionary keys as column header & value will be used as list or row 
   'age':[25,26,27]  
}
myvar=pd.DataFrame(mydataset)
myvar2=pd.Series(mydataset)     # it has no column labels, as written in single column 
print(myvar2)
print(myvar)
myvar['liss'].max()

# pandas use loc attribute to one or more specifie row(s)
print(pd.loc[0,1,2])


#load files into a dataframe
df=pd.read_csv('data.csv')
print(df)

#to print entire dataframe
print(df.to_string())


#to check the maximum number of the rows 
print(pd.options.display.max_rows)