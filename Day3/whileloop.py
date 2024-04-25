#whileloop
i = 1
while i < 7:
    print(i)
    i += 1

#break statement
i = 1
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1
#continue
i = 1
while i < 7:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print("execute querry")


