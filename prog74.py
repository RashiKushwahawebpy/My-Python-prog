#Write a Python program to rotate a list to the right by one position.
numbers = list(map(int, input("Enter List: ").split()))
last = numbers[-1]
numbers.pop()
numbers.insert(0, last)
print("Rotated List =", numbers)