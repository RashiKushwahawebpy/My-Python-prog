# program to calculate the electricity bill. If the total amount is greater than ₹5000, apply a 10%
# discount; otherwise, no discount.
units = int(input("Enter Units Consumed: "))
rate = float(input("Enter Rate Per Unit: "))
bill = units * rate
if bill > 5000:
	discount = bill * 0.10
else:
	discount = 0
finalbill = bill - discount
print("Total Bill =", bill)
print("Discount =", discount)
print("Amount Payable =", finalbill)