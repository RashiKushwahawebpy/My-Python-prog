# Income Tax Slab
income = int(input("Enter Annual Income: "))
if income <= 300000:
	print("No Tax")
elif income <= 700000:
	print("5% Tax")
elif income <= 1000000:
	print("10% Tax")
else:
	print("20% Tax")