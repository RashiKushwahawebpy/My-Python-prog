#Write a program to count the total number of words in a file. 
file = open("students.txt", "r") 
text = file.read() 
words = text.split() 
print("Total Words =", len(words)) 
file.close() 