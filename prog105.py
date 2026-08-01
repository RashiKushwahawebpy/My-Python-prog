#Write a program to append new student names to an existing file. 
file = open("students.txt", "a") 
name = input("Enter New Name: ") 
file.write(name + "\n") 
file.close() 
print("Record Added") 