student = {
 "Roll":41,
 "Name":"Rashi",
 "Course":"CSE",
 "Marks":89
}
key = input("Enter Key: ")
if key in student:
    print("Value =", student[key])
else:
    print("Key Not Found") 