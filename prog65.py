#Write a recursive function to print numbers from N to 1. 
def countdown(n):
	if n == 0:
		return
	print(n)
	countdown(n - 1)
num = int(input("Enter Number: "))
countdown(num) 