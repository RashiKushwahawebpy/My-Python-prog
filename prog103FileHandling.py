# A Write a program to create a text file and store five student names. 
file = open("students.txt", "w")
for i in range(5): 
    name = input("Enter Name: ") 
    file.write(name + "\n") 

file.close() 

print("Data Saved Successfully") 