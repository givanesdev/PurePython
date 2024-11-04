#Built-in functions
y=max(34,56,107, 95)
print(y)

x=min(35,49,6,90,27,6)
print(x)

z=pow(2,3)
print("The result is", z)

#User-defined functions
def greet():
    print("Hello Givanes")
greet() #calling the function

def product():
    a=12
    b=10
    print(a*b)
product()

#parameters/variable and arguments/values
def add(x,y):

    print(x+y)
add(4,5)
add(20,30)

def add(x=3,y=5):

    print(x+y)
add()

def employee(fullname,age,position, marital_status):
    print(fullname,age,position,marital_status)
employee("Giv Wakasa", 30, "Manager", "married")
employee("Charty", 30, "CEO", "married")
employee("Tamra", 20, "Director", "single")
employee("Olv", 27, "HR", "single")
employee("Ted", 20, "Dep-Director", "single")