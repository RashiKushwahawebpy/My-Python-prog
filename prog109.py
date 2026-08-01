#Write a program to copy one file into another. 
source = open("students.txt", "r") 
destination = open("backup.txt", "w") 
destination.write(source.read()) 
source.close() 
destination.close() 
print("File Copied Successfully")
