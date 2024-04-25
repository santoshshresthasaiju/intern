#class blueprint
class student:
    name = "san"
n = student()
print(n.name)

# the __init__() functions
class student:
    def __init__(self,name,age):
        self.name =name
        self.age = age
n = student("san",24)
print(n.name)
print(n.age)

#the __str__() functions
class student:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def __str__(self) -> str:
        return f"{self.name}({self.age})"
n = student("san",24)
print(n)

#object methods
class student:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def func(self):
        print("This is Mr. " + self.name)
n = student("san",24)
n.func()

#self parameter
class student:
    def __init__(defining,name,age):
        defining.name =name
        defining.age = age
    def func(ams):
        print("This is Mr. " + ams.name)
n = student("san",24)
n.func()

#modify
class student:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def __str__(self) -> str:
        return f"{self.name}({self.age})"
n = student("san",24)
n.age =40
print(n)

#del
class student:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def __str__(self) -> str:
        return f"{self.name}({self.age})"
n = student("san",24)
print(n)

