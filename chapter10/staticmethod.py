class main:
    name="manish"
    langauge="python"
    @staticmethod               #no need to write the self keyword 
    def staticmethod():
        print(f"iam {2+3}static method look upward.")
    def getInfo(self):
        print(f"name is {self.name} and langauge is {self.langauge}")
    @staticmethod
    def display(self):
        print(f"{self.name} is a name and the language is {self.langauge}")
obj=main()
obj.staticmethod()
obj.getInfo()