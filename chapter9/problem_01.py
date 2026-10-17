#find the string in the given file 
with open("water_bot.txt") as f:
    content=f.read()
    if("water" in content):
        print("water keyword is found in the content")
    else:
        print("water keyword doesn't exist :")
