#forloop
Itemset = ["java","c","c++","sklearn","python","django","frappe"]
for x in Itemset:
    print(x)
#break
Itemset = ["java","c","c++","sklearn","python","django","frappe"]
for x in Itemset:
    print(x)
    if x == "python":
        break

#continue
Itemset = ["java","c","c++","sklearn","python","django","frappe"]
for x in Itemset:
    if x == "python":
        continue
    print(x)


for x in range(6):
    print(x)
for x in range(1,3):
    print(x)
for x in range(2,15,3):
    print(x)
#pass statement is used to avoid getting errors

for x in [0,2,3,44,3,2]:
    pass

