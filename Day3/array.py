#python does not have build in array but it used list as an array
student = ["san","man","kam","jun","mon"]

x =student[3]
print(x)

student[0] = "kam"
print(student)
x = len(student)
print(x)
student.append("sam")
print(student)
student.pop(5)
print(student)
