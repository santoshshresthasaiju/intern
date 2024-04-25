#create a parent class
class student:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname =lname
    def printname(self):
        print(self.fname ,self.lname)
n = student("sam","shre")
n.printname()

#child class
class Student1(student):
    pass

class student:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname =lname

    def printname(self):
        print(self.fname ,self.lname)

class Student1(student):
    def __init__(self, fname, lname):
        super().__init__(fname, lname) # supr() functions is used to make child class
        #inherit all the methods  and properties
        self.graduationyear = 2024
n = Student1("san","stha")
print(n.graduationyear)
