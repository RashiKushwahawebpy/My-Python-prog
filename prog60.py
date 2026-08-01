#Write a recursive function to calculate the power of a number (xⁿ). 
def power(x, n):
	if n == 0:
		return 1
	return x * power(x, n - 1)
base = int(input("Enter Base: "))
exp = int(input("Enter Exponent: "))
print("Answer =", power(base, exp))