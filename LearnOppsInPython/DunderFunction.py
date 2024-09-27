'''
Summary of Common Dunder Methods
Dunder Method	Usage
__init__	Constructor method
__str__	String representation
__repr__	Official string representation (for debugging)
__len__	Length of the object
__getitem__	Indexing behavior
__setitem__	Assignment behavior for indices
__call__	Make an object callable like a function
__eq__, __lt__, etc.	Comparison operators
__add__	Addition behavior
'''
class MyNumber:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return MyNumber(self.value + other.value)

    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value

#Example usage
num1 = MyNumber(10)
num2 = MyNumber(20)

print(num1 == num2)  # Output: False
print(num1 < num2)   # Output: True
num3 = num1 + num2
print(num3.value)  # Output: 30

class MyList:
    def __init__(self, items):
        self.items = items
    
    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

#Example usage
#Get item dunder function example usgae
my_list = MyList([10, 20, 30])
print(my_list[1])  # Output: 20

#Set item dunder function example usgae
my_list = MyList([10, 20, 30])
my_list[1] = 50
print(my_list.items)  # Output: [10, 50, 30]

class MyClass:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"MyClass with name {self.name}"

#Example usages
obj = MyClass('Python')
print(obj)  # Output: MyClass with name Python




