class main:
    name="manish"
    langauge="python"
    def __init__(self,name,langauge,salary):                 #constructor dunder method 
        self.name=name
        self.langauge=langauge
        self.salary=salary
        print(f"name:{self.name}\n langauge:{self.langauge}\n salary:{self.salary}")
        print("I called myself without creating object because iam dunder method")
    def getInfo(self):
        print(f"name is {self.name} and langauge is {self.langauge}")
obj=main("sohan","ML",20000)
obj.getInfo()