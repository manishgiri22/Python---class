a=34
def function():
    global a            #its makes varible global in fuction also so its changed the value  globally 
    a=3
    print(a)
function()
print(a)