#iterator is an object that contains a countable number of values
#__iter__() and __next__()

tup = ("python","Ml","Ai","Sklearn")
myv = iter(tup)

print(next(myv))
print(next(myv))
print(next(myv))
print(next(myv))

tup = ("python","Ml","Ai","Sklearn")
for x in tup:
    print(x)

#create an iterator
class numbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x =self.a
        self.a += 1
        return x

myclass = numbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#stop iterations
class numbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x =self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = numbers()
myiter = iter(myclass)

for x in myiter:
    print(x)