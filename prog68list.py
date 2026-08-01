numbers = []
n = int(input("How many numbers? "))
for i in range(n):
 value = int(input("Enter Number: "))
 numbers.append(value)
largest = max(numbers)
smallest = min(numbers)
average = sum(numbers) / len(numbers)
print("Original List :", numbers)
print("Largest :", largest)
print("Smallest :", smallest)
print("Average :", average) 