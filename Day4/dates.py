import datetime
x =datetime.datetime.now()
print(x)


print(x.year)
print(x.strftime("%A"))
print(x.strftime("%a")) #striftime() is a method to access datetime in readable
print(x.strftime("%w"))
print(x.strftime("%d"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%x"))

y = datetime.datetime(1999,11,26)
print(y)