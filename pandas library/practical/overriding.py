class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Polymorphic behavior
# animals = [Dog(), Cat(), Animal()]
c=Animal()
a=Dog()
b=Cat()
print(c.sound())
a.sound()
b.sound()

