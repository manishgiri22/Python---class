# try:
#     a=int(input("enter a number"))
#     b=int(input("enter a divisor"))
#     if (b!=0):
#         res=a>b
#         print(res)
#     else:
#         raise ZeroDivisionError
# except Exception as e:
#     print(e)
# # except (ZeroDivisionError,TypeError,NameError,ValueError) as e:
# #     print(e)
# finally:
#     print("divison is successfully completed ")


try:
    age=int(input("enter the age of the voter"))
    if (age>18):
        print("you're capable for the voting ")
    else:
        raise ValueError("voter can't be under 18")
except Exception as e:
    print(e)
finally:
    print("everyone should vote if you're authentic user")


