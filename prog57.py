# Car Insurance Problem
age = int(input("enter age of driver:"))
acc = int(input("no of accident in 3 years:"))
cost = int(input("cost of vehicle:"))
manuf = input("car manufacture:")
insuAmt=0
excess=0
PType=" "
if age >= 25:
	if manuf =='I':
		if acc == 0:
			charges = 6
			excess = 0
		else:
			charges = 7
			excess = 100
			PType = 'C'
	else:
		if acc == 0:
			charges = 6
			PType = 'C'
			excess = 100
		else:
			charges = 7
			excess = 0
			PType = 'T'
else:
	if manuf == 'I':
		if acc == 0:
			charges = 6
			excess = 100
			PType = 'C'
		else:
			if acc == 0:
				PType = 'C'
	else:
		PType = 'NP'
		charges = 8
		excess = 100
		insuAmt = cost*charges/100
		print("type of motor insurance policy:",PType)
		print ("the amount of the premium:",insuAmt)
		print("excess payable on any claim if applicable:",excess)
# Program end 