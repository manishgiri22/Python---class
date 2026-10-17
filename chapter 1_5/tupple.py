# a=(2,33,"manish","laita")
# print(a)
# print(type(a))
# # print(a.count(2))
# # print(a.index('manish'))
# # # good night  tupple 
# tupple=('manish','giri','rohan','sapkota',2020)
# print(tupple)
# print(type(tupple))
# print(len(tupple))  #len() function is used to find the length of the tupple 
# t=("manish",'giri',22,"rohan")
# l=list(t)
# l.append("lalit")
# tuple(l)
# print(l)


#loops in tuple 
    #for loop 
t=(1,2,3,4,5,6,70,8,9)
for i in range(len(t)):
    print(t[i])
    #while loop
i=0
while i<len(t):
    print(t[i])
    i+=1
    #use to count the repeatation of the item in tuple 
print(t.count(2))
#use to find the index of the item in tuple
print(t.index(70))
