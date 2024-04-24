#Booleans values(true/false)
x = 5
y = 3
if y > x:
    print("y is greater")
else:
    print("x is greater")

print(bool(x))
print(bool(y))

# any values with (),{},[],"",0 and none are evaluate to False
class python():
    def __len__(self):
        return 0    #len function that returns 0 or false evaluates as false
myobj = python()
print(bool(myobj))

#operators
x += 3
print(x)
x *= 4
print(x)
y %= 3
print(y)
print(x := 300)

# Comparision operator
a = 4
b = 5
print(">")
if(a > b):
    print(a)
else:
    print(b)
print("!=")
if(a != b):
    print(a)
else:
    print(b)
print(">=")
if(a >= b):
    print(a)
else:
    print(b)

# and , or ,not ,is , is not, in , in not 
#list access items 

items = ["red","green","yellow","banana"]
print(items[1])

#negative indexing
items = ["red","green","yellow","banana"]
print(items[-2])
print(items[2:5]) #range 

#checking yellow in this list
items = ["red","green","yellow","banana"]
if "yellow" in items:
    print("yes,'yellow is in the items list")

#change in list items yellow by pinkl

items = ["red","green","yellow","banana"]
items[2] = "pink"
print(items)

#insert() items
items = ["red","green","yellow","banana"]
items.insert(1, "black")
print(items)
# to add items at last append() method is used
items = ["red","green","yellow","banana"]
items.append("purple")
print(items)


#extend list
items = ["red","green","yellow","banana"]
nextitems = ["white","orange","pink","voilet"]
items.extend(nextitems)
print(items)

#to remove list
items = ["red","green","yellow","banana"]
items.remove("banana")
print(items)

#pop() method removes specified index
items = ["red","green","yellow","banana"]
items.pop(3)
print(items)

#del is used to remove specified index or complete list
items = ["red","green","yellow","banana"]
del items[1]
print(items)
del nextitems

# clear() empities the list

#loop lists
#for
items = ["red","green","yellow","banana"]
for x in items:
    print(x)

items = ["red","green","yellow","banana"]
for i in range(len(items)):
    print(items[i])
  
print("while loop")
items = ["red","green","yellow","banana"]
i = 0
while i < len(items):
    print(items[i])
    i = i + 1

#list comprehension

items = ["red","green","yellow","banana"]
newitems = []

for x in items:
    if "w" in x:
        newitems.append(x)
print(newitems)

items = ["red","green","yellow","banana"]
newitems = [x for x in items if x != "banana"]
print(newitems)

newitems = [x for x in range(10)]
print(newitems)

#shorting the list

items = ["red","green","yellow","banana"]
items.sort()
print(items)

# sort desending

items = ["red","green","yellow","banana"]
items.sort(reverse = True)
print(items)


def func(n):
    return abs(n -50)
num =[6, 7, 8, 9]
num.sort(key = func)
print(num)

items = ["red","green","yellow","banana"]
lists = items.copy()
print(lists)

#join two list
items = ["red","green","yellow","banana"]
nextitems = ["white","orange","pink","voilet"]

newlist = items + newitems #items.append() or extends
print(newlist)


#tupples 

mtuple = ("python","django","sklearn","ML")
print(len(mtuple))

# tuple can contain diff data types
#tuple can also use as tuple()constructor
#ptuple = mtuple(("python","django","sklearn","ML"))
#print(ptuple)

#tuple convert into a list(confusion on this)

#mtuple = ("python","django","sklearn","ML")
#a = list(mtuple)
#a.append("AI")
#mtuple = tuple(a)
#print(mtuple)

#adding tuple
mtuple = ("python","django","sklearn","ML")
atuple = ("java","c","c++","c#")

mtuple += atuple
print(mtuple)

#using Asterisk
mtuple = ("python","django","sklearn","ML")
(java, *tropic, c) = mtuple
print(java)
print(tropic)
print(c)

# loop for tuple
mtuple = ("python","django","sklearn","ML")
for x in mtuple:
    print(x)

#range and len
mtuple = ("python","django","sklearn","ML")
for i in range(len(mtuple)):
    print(mtuple[i])

#multiply tuples
mtuple = ("python","django","sklearn","ML")
ptuple = mtuple * 2
print(ptuple)

#Tuple methods
#count()
#index()

#set 
itemset = {"python","django","sklearn","ML"}
print(itemset)

#add items
itemset = {"python","django","sklearn","ML"}
itemset.add("java")
print(itemset)

#update()
itemset = {"python","django","sklearn","ML"}
additemset = {"java","c","c++","c#","python"}

itemset.update(additemset)
print(itemset)

#we can add by update() method any object(tuples,lists,dict)
#remove()
#discard()
#pop()
#clear()
#del

#loop
itemset = {"python","django","sklearn","ML"}

for i in itemset:
    print(i)


#union()
usets = itemset.union(additemset)
print(usets)

#intersections
usets = itemset.intersection(additemset)
print(usets)

itemset = {"python","django","sklearn","ML"}
additemset = {"java","c","c++","c#","python"}
usets = itemset.difference(additemset)
print(usets)
print("update")
usets = itemset.difference_update(additemset)
print(usets)
print("sydiff")
usets = itemset.symmetric_difference(additemset)
print(usets)
print("symdup")
usets = itemset.symmetric_difference_update(additemset)
print(usets)


#Dictionary
dictl ={
    "language" : "python",
    "year" : 1991,
    "created by":"Guido van Rossum"
}

x = dictl.items()
print(x) #before
dictl["year"]= 2024
print(x) #after

#checking if key exists
dictl ={
    "language" : "python",
    "year" : 1991,
    "created by":"Guido van Rossum"
}
if "language" in dictl:
    print("yes")

#change values
dictl ={
    "language" : "python",
    "year" : 1991,
    "created by":"Guido van Rossum"
}
dictl["created by"] = "Santosh Shrestha"
print(dictl)

dictl.update({"year" : 2024})
print(dictl)

dictl["Name"] = "Santosh Shrestha"
print(dictl)

dictl.pop("Name")
print(dictl)
