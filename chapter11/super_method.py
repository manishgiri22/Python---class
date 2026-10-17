class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        print(f"{self.name}, {self.age}, {self.salary}")

class Manager(Employee): 
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department
        print(f"Manager manages {self.department} only:")

# Creating an object of the Manager class
obj = Manager("manish", 23, 24000, "IT")
