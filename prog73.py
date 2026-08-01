#Write a Python program to input N numbers into a list and print the second largest number.
numbers = []
n = int(input("How many numbers? "))
for i in range(n):
    value = int(input("Enter Number: "))
    numbers.append(value)
numbers = list(set(numbers))
numbers.sort()
print("Second Largest =", numbers[-2]) 