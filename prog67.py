#Write a function to find the second largest element in a list entered by the user. 
def second_largest(lst):
	largest = second = -999999
	for i in lst:
		if i > largest:
			second = largest
			largest = i
		elif i > second and i != largest:
			second = i
			return second
	numbers = list(map(int, input("Enter Numbers: ").split()))	
	print("Second Largest =", second_largest(numbers))