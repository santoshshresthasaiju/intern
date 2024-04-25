#functions
def my_function():
    print("begain in the functions")

def func():
    print("python is a snake and language")
func()

#passing arguments
def func(fname):
    print(fname + "" "Shrestha")
func("Santosh")
func("Rejina")
func("Kala")

#defining number of arguments
def func(fname, laname):
    print(fname + " " + laname)
func("Santosh", "Shrestha")

#arbitary arguments,*args
def product(*items):
    print("The name of this product is " + items[1])

product("Current","rumpum","chocolate","santoor")

#arbitary keyword arguments
def func(**college):
    print("The course we study in this college is " + college["coursename"])
func(collegename = "birendra",coursename= "Bsc.CSIT")

#default parameter value
def func(country = "Nepal"):
    print("I am form " + country)

func()
func("USA")
func("Canada")
func("Austrila")

#passing lists as a arguments
def func(language):
    for x in language:
        print(x)
Plang = ["c","c++","python","java"]
func(Plang)

#returning value

def func(x):
     return 5 * x
print(func(5))

#positional-only argu , /

#keyword only
def college(*, x):
  print(x)

college(x = "Birendra")

#recursion
def tri_recursion(x):
  if(x > 0):
    result = x + tri_recursion(x - 2)
    print(result)
  else:
    result = 0
  return result

print("Results")
tri_recursion(10)