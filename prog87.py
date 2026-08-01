#Write a Python program to find the three most common characters in a string.
from collections import Counter
text = input("Enter String: ")
count = Counter(text)
print(count.most_common(3)) 