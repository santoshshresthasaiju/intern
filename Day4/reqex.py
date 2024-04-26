import re
txt = "I am learning python basics programming language"
x =re.search("I.*basics$",txt)  #start with I and ends with basics

if x:
    print("yes! matched")
else:
    print("no match")
#findall function matches the contain
x = re.findall("a",txt)
print(x)

#split
x = re.split("\s",txt) 
print(x)

#sub()
x = re.sub("\s", ",", txt)
print(x)

x = re.search(r"\bl\w+", txt)
print(x.span())
print(x.string) #.string()
# .group()
print(x.group())


