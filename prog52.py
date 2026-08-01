# program to check inputted number is Armstrong number or not
n = int(input("3 digit no"))
s = 0
p = n
while n != 0:
	k = n % 10
	s = s + (k*k*k)
	n = n // 10
if (p == s):
	print("{0}is an Armstrong number".format(p))
else:
	print("Not Armstrong number") 
