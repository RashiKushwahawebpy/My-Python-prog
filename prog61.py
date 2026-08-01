#Write a recursive function to find the sum of digits of a number. 
def digit_sum(n):
	if n == 0:
		return 0
	return n % 10 + digit_sum(n // 10)
num = int(input("Enter Number: "))
print("Sum of Digits =", digit_sum(num)) 