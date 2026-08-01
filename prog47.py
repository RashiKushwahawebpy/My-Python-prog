# program for HCF
try:
	a = int(input("enter first numbers: "))
	b = int(input("enter second number: "))
	while b!=0:
		a, b = b, a % b
	print(f"{a} is the HCF")
except ValueError:
	print("invalid input! please enter whole numbers only.")	