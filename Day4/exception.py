#try except
# try block lets to check code for errors
#except handle the error
#else execute code when no error
#finally execute code

# try:
#     print(x)
# except:
#     print("an exception occured")


# #NameError
# try:
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("something else went wrong")

try:
    print("python")
except:
    print("something wrong")
else:
    print("nothing wrong")
finally:
    print("The try except is done")

#raise
x = -12

if x<0:
    raise Exception("Sorry, no number")