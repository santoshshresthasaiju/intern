#syntax for python execution
#python p.py(file name)
import sys 
print(sys.version)  #to check the python version of the editor


print("Hello World!!!")


# hash(#) is used for the comment single line
#multiline Comment
"""
a = 1
b = 2
print(a+b)

"""

#Python Variables
a = 4
b =5
print(a*b)
#castingy 
x =str(4)
y = int(5)
z = float(2)



x="samip" #x and y are type str
y=9

print(x , y)

print(type(x)) #to get the data type of a variable by type()function
print(type(y))

#python - VariiableNames
#legal variables
myvar ="santosh"
my_var = "suman"
_my_var_ ="sisan"
MYVAR ="sandeep"

Product = "list of product"

#to assign multiples variables
x, y, z = "Python", "Django", "C"
print(x)  #in c++ variables is assign by defining type 
print(y)
print(z)
#we can assign one value to multiple variables
x= y= z = "Python"
print(x) 
print(y)
print(z)

#output variables - print() function is uesd
a ="I am a programmer"
print(a)

#global variables
#global variables can be used by everyone on both inside and outside functions

a ="programmer"

def myfunc():
    a = "writter"
    print("I am a " + a)
myfunc()
print("I am a " + a)

#using keyword global
 
a ="programmer"

def myfunc():
    global a
    a = "writter"
    
myfunc()
print("I am a " + a)

#data types
"""
set type : str 
numeric types: int,float,complex
sequences types: list,tuple,range
mapping type: dict
set types : set, frozenset
boolean type: bool
binary types: bytes,bytearray,memoryview
none type: nonetype

"""

x = "programmer" #str
x =1 #int
x =1.34 #float
x =2j #complex
x= ["php","python","django","c++"] #list it is used to store multiple items in a single variables.
#tuples

language =("php","python","django","c+{+") #it is unchangeable where list is changeable

#dict it is used for storing data values in key:value pairs form.
dictl ={
    "language" : "python",
    "year" : "1991",
    "created by":"Guido van Rossum"
}
print(dictl)
x = dictl["year"]

#using get() method
x =dictl.get("year")
print(x)
#get key
x =dictl.keys()
print(x)
#get values
x =dictl.values()
print(x)