'''class Complexnumber:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,other):
        return f"{self.real+other.real}+{self.imaginary+other.imaginary}i"
c1=Complexnumber(2,3)
c2=Complexnumber(4,5)
print(c1+c2)'''

# #example 2
# class Voter:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __gt__(self,x,y):
#         if self.age>x.age and self.age>y.age:
#             return True
#         if x.age>self.age and x.age>y.age:
#             return True
#         else:
#             return False 
# v1=Voter("manish",19)
# v2=Voter("manoj",20)
# v3=Voter("sohan",12)
# if(v1>v2 and v1>v3):
#     print (f"{v1.name} is the voter")
# elif(v2>v1 and v2>v3):
#     print (f"{v2.name} is the voter")
# else:
#     print (f"{v3.name} is the voter")


# exampl3
class Complexsub:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __sub__(self,other):
        return f"{self.real-other.real}+{self.imaginary-other.imaginary}i"
c1=Complexsub(2,4)
c2=Complexsub(4,5)
print(c1-c2)