class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute


    def display_employee(self):
        return f"Name: {self.name}, Salary: {self.__salary}"



emp = Employee("John", 50000)
print(emp.display_employee())
