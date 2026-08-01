#Write a program to reverse a string without using slicing.
text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reverse =", reverse)
