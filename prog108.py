#Write a program to count the total number of characters in a file.
file = open("students.txt", "r") 
text = file.read() 
print("Characters =", len(text)) 
file.close() 