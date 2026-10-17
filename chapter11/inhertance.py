class Employee:
    company="info tech"
    def info(self,name,salary):
        self.name=name
        self.salary=salary
        print(f"employee work in {self.company} and name is {self.name} salary:{self.salary}")

class department(Employee): #inheritance from the employee class
    d_no=20
    def getin(self,did):
        self.did=did
        print(f"{self.did} emplyoee work on d_no{self.d_no}")
# e=Employee()
# e.info("sai",50000) 
d=department()
d.getin(10)
d.info("sai",50000)  #inherit method from employee call in depatment class object 