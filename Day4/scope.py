#variable only available from inside the region
#local scope
def myfunc():
    name = "sant"
    print(name)
myfunc()

#function inside function
def func():
    a = 1200
    def innerfunc():
        print(a)
    innerfunc()

func()

#global scope
a=123
def func():
    print(a)
func()
print(a)

#global keyword
def func():
    global x
    x = 200

func()
print(x)

#nonlocal
def func():
  x = "bmc"
  def func1():
    nonlocal x
    x = "college"
  func1()
  return x

print(func())