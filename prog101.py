#Write a program to count uppercase and lowercase letters.
text = input("Enter string: ")
 
upper = lower = 0

for ch in text:
    if ch.isupper():
        upper =+ 1
    elif ch.islower():
        lower =+ 1 
print("Uppercase =", upper)
print("Lowercase =", lower)
