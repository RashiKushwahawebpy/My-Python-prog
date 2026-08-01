#function counts the number of uppercase letters, lowercase letters, digits, and special characters in a string. 
def count_characters(text):
	upper = lower = digit = special = 0
	for ch in text:
		if ch.isupper():
			upper += 1
		elif ch.islower():
			lower += 1
		elif ch.isdigit():
			digit += 1
	else:
		special += 1
	print("Uppercase =", upper)
	print("Lowercase =", lower)
	print("Digits =", digit)
	print("Special Characters =", special)
	s = input("Enter a string: ")
	count_characters(s)