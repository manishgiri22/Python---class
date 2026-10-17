#farenheight to celcius in python 
def f_to_c(f):
    c=5*(f-32)/9
    return c
f=int(input("enter farenheight to calculate in celcius: "))
c=f_to_c(f)
print(f"{f} farenhight to celcius value is {round(c,2)}")

# avoid new line in the end in the print function 
print("a")
print("b")
print("c",end="") #this cleared or prevent the new line 
print("d",end="")