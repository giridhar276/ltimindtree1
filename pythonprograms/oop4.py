# class definition
class Employee:
    # constructor
    # constructor is invoked automatically when object gets created
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
    def displayEmployee(self):
        print("Employee name :",self.name)
        print("employee age  :",self.age)
        print("employee city :",self.city)


# object intialization
emp1 = Employee("rita",25,"Hyd")
emp1.displayEmployee()

emp2 = Employee("sita",22,"bang")
emp2.displayEmployee()

emp3 = Employee("gita",21,"chennai" )
emp3.displayEmployee()
