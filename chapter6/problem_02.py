mark1=int(input("enter the first marks:"))
mark2=int(input("enter the second marks:"))
mark3=int(input("enter the third mark:"))
total_percentage= (100 * (mark1+mark2+mark3))/300
if(total_percentage>40 and mark1>33 and  mark2>33 and mark3>33):
    print("you are passed: you get total:",total_percentage,"percentage")
else:
    print("you are failed please try again next year:")
