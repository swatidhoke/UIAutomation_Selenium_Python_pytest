class Animal:
    def speak(self):
        return "This animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "The dog barks"

dog = Dog()
print(dog.speak())  # Output: The dog barks


'''
This is example of SUPER METHOD
'''

class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Start the car")
    
    @staticmethod
    def stop():        
        print("Stop the car")

class Toyota(car):
    def __init__(self,name,  type):
        #use the super class variblle like below
        super().__init__(type)
        #This is Tpypta class varible
        self.name = name


car1 = Toyota("prius", "electric")
print(car1.type)