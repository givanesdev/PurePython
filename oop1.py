class Student:
    #properties/variables/characteristics/attributes
    name="Givanes"
    gender="Male"
    age= 101

    #behaviour/methods/function
    def study(self):
        print("Student is studying")

#object1
student1=Student()  #creating an object
student1.study()
print(student1.name)
print(student1.age)

#object2
student2= Student()