class Employee:
    salary=230
    increment=23
    @property
    def afterincrementsalary(self):
        return self.salary +self.salary *(self.increment/100)
    @afterincrementsalary.setter
    def afterincrementsalary(self,salary):
        self.increment= ((salary/self.salary)-1)*100
c=Employee()
c.afterincrementsalary=2000
print(c.increment)