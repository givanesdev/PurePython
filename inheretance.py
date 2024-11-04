class Animal: #parent class
    def speak(self):
        print("animal is speaking")

class Dog(Animal):    #child class
    def bark(self):
        print("Dog is barking")

animalA = Animal()
animalD=Dog()
animalD.speak()