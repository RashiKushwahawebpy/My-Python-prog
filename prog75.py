#Write a Python program to create two lists containing positive and negative numbers separately.
numbers = list(map(int, input("Enter Numbers: ").split()))
positive = []
negative = []
for num in numbers:
 if num >= 0:
    positive.append(num)
 else:
    negative.append(num)
print("Positive List =", positive)
print("Negative List =", negative) 