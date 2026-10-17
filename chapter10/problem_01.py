class programmer:
    post="programmer"
    def __init__(self, name, age, post):
        self.name=name
        self.age=age
        self.post=post
    def getInfo(self):
        print(f"Name: {self.name}, Age: {self.age}, Post: {self.post}")
manish=programmer("manish",23,"senior developer")
manish.getInfo()