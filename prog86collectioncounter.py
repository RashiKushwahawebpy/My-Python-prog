#Write a Python program to count the frequency of every word in a sentence using counter.
from collections import Counter
sentence = input("Enter Sentence: ")
words = sentence.split()
frequency = Counter(words)
print("Word Frequency")
for word, count in frequency.items():
    print(word, "=", count) 
