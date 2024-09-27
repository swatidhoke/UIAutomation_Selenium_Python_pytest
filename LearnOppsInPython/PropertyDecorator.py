'''
@property Decorator:

The @property decorator allows you to define a method in a class that can be accessed like an attribute, without the need to call it explicitly. In the example above, calcAveMarks is a method, but it can be accessed like a simple attribute (i.e., student1.calcAveMarks instead of student1.calcAveMarks()).

It’s particularly useful when you want to calculate or derive a value dynamically but present it as a read-only property of the class. It avoids the need to call a method explicitly while still computing the result.

Why Use @property:

It improves code readability because you can access a method like an attribute.
It encapsulates logic, allowing you to compute or modify values without exposing them directly as attributes.

'''
class Student:
    def __init__(self, name, phymarks, mathmarks):
        self.name = name
        self.phymarks = phymarks
        self.mathmarks = mathmarks

    @property 
    def calcAveMarks(self):
        return (self.phymarks + self.mathmarks) / 2

# Creating an instance of the Student class
student1 = Student("John", 80, 90)
print(f"Average Marks: {student1.calcAveMarks}")
