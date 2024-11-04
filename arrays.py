courses =["MIT","Data Science","CyberSecurity"]

#Accessing element in ana array using index position
print(courses[0])

#Looping through an array
for y in courses:
    print("Course is",y)

#adding a new element
courses.append("Android Development")
print(courses)

#Deleting an element
courses.remove("MIT")