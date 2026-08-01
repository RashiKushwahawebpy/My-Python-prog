#Write a program to search for a word in a file.
file = open("students.txt", "r") 
text = file.read() 
word = input("Enter Word to Search: ")
if word in text: 
    print("Word Found")
else: 
    print("Word Not Found") 
file.close() 