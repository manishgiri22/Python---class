class A:
    a=20
class B(A):
    b=30
class C(B):
    c=40
ob_a=A()                #have access of only class A
print(ob_a.a)           
ob_b=B()                #have access of  class A and B 
print(ob_b.a,ob_b.b)
ob_c=C()                #hace access of class A,B,C
print(ob_c.a,ob_c.b,ob_c.c)