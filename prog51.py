# program to find the sum of digits of a given no
n = int(input("Enter a four digit number:"))
s = 0
p = n
while n != 0:
	k = n % 10
	s = s + k
	n = n // 10
print("sum of digits={0}".format(s))

