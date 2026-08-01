#Write a program to count the number of lines in a text file. 
file = open("students.txt", "r")
count = 0 
for line in file: 
    count += 1 
file.close() 
print("Total Lines =", count) 