class Person:
    def __init__(self, name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def movement(self):
        print("Person is walking")

person1 = Person("Givanes","M",109)
person2 = Person("Wakala","M",99)
person3 = Person("Ramsey","M",129)

print(person1.name)
print(person2.name)
print(person3.name)