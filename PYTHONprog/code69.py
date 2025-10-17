class Employee:
    CompanyName = "Apple"

    def show(self):
        print(f"Name of the employee is {self.name} and the company name is {self.CompanyName}")
    
    @classmethod
    def changeCompany(cls, newCompany): # you can put any other word than cls, it will take it as a first arguement just like 'self'
        cls.CompanyName = newCompany

emp1 = Employee()
emp1.name = "Sam"
emp1.show()
emp1.changeCompany("Google")
emp1.show()
# now does this means the class variable 'CompanyName' has been changed?

print(Employee.CompanyName) # no it won't it will be same

# however if you wanna change the class variable, which in this case is CompanyName, then  you gotta put a @classmethod decorator just above the chnage company method
# now if you run the same above code, print(Employee.CompanyName) then this will return the changed name