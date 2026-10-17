fp=open("manish.txt",'w')
fp.write("manish giri ho mero naam ")
fp.close()
with open('manish.txt','r') as fp:
    text=fp.read()
    text.replace("manish","sohan")
    for letter in text:
        print(letter,"\n")