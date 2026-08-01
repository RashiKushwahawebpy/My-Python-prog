#Write a program to display only the lines containing a specific word. 
keyword = input("Enter keyword: ")
file = open("students.txt", "r") 
for line in file: 
    if keyword.lower() in line.lower():
         print(line, end="") 
         
file.close() 