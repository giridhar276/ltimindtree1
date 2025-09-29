
# class definition
class Employee:
    def getEmployee(self,name):
        self.name = name
    def displayEmployee(self):
        print("Employee name :",self.name)


# object intialization
emp1 = Employee()
# invoked method
emp1.getEmployee("rita")
emp1.displayEmployee()
emp2 = Employee()
# invoked method
emp2.getEmployee("rita")
emp2.displayEmployee()
emp3 = Employee()
# invoked method
emp3.getEmployee("rita")
emp3.displayEmployee()
