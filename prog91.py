#Write a Python program to remove duplicate characters from a string.
text = input("Enter String: ")
result = ""
for ch in text:
    if ch not in result:
        result += ch
print("After Removing Duplicates =", result) 