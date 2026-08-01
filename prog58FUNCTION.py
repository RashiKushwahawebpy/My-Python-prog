# Function to calculate sum of cubes
def sum_of_cubes(n):
	total = 0
	for i in range(1, n + 1):
		total = total + i ** 3
		return total

num = int(input("Enter N: "))
print("Sum of Cubes =", sum_of_cubes(num)) 