class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Bark"

def animal_sound(animal):
    print(animal.sound())

cat = Cat()
dog = Dog()
animal_sound(cat)  # Output: Meow
animal_sound(dog)  # Output: Bark
