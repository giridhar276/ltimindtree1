
# class definition
class Employee:
    # constructor
    # constructor is invoked automatically when object gets created
    def __init__(self,name):
        self.name = name
    def displayEmployee(self):
        print("Employee name :",self.name)


# object intialization
emp1 = Employee("rita")
emp1.displayEmployee()

emp2 = Employee("sita")
emp2.displayEmployee()

emp3 = Employee("gita" )
emp3.displayEmployee()
