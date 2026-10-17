#create a pet class from animal . further create class dog from pets and create method in dog bark
class animal:
    pass
class pet(animal):
    pass
class dog(pet):
    @staticmethod #to not to use self keyword
    def bark():
        print("byau byau byau .... ")
d=dog()
d.bark()