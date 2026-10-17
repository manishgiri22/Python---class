word="machikne"
with open("water_bottle.txt","r") as f:
    content=f.read()
newcontent=content.replace(word,"M*******")
with open("water_bottle.txt","w") as f:
    f.write(newcontent)