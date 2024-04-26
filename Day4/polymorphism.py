#polymorphism
#many forms methods/functions/operators
#function polymorphism
#string len()
x ="python"
print(len(x))

mytuple = ("java","python","sklearn","django")
print(len(mytuple))

dictn ={
    "brand":"Bmw",
    "model":"2024",
    "color":"black"
}
print(len(dictn))

#class Polymorphism
class student:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname =lname

    def move(self):
        print("Csit")
class student1:
    def __init__(self,fname,lname):
        self.fname =fname
        self.lname =lname
    def move(self):
        print("Bit")
class student2:
    def __init__(self,fname,lname):
        self.fname =fname
        self.lname =lname
    def move(self):
        print("Bca")        
student11 =student("san","stha")
student111 =student1("kam","stha")
student211 =student2("ru","dhal")
for x in (student11,student111,student211):
    print(x.fname)
    print(x.lname)
    x.move()
