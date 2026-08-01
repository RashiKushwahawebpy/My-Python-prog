#Write a program to safely open a file using exception handling.
try: 
    file = open("students.txt", "r") 
    print(file.read()) 
    file.close() 
    
except FileNotFoundError: 
    print("File does not exist.") 