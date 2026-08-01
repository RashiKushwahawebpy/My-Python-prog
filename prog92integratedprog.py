#Write a Python program to input a sentence, store its words in a list, count word frequency 
# using Counter, and store unique words in a deque.
from collections import Counter, deque
sentence = input("Enter Sentence: ")
word_list = sentence.split()
print("Word List =", word_list)
frequency = Counter(word_list)
print("\nWord Frequency")
for word, count in frequency.items():
    print(word, "=", count)
unique_words = deque(frequency.keys())
print("\nDeque of Unique Words")
print(unique_words) 