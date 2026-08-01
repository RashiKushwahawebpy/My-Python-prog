#6. List with Variable Length (* operator)
numbers = [1, 2, 3, 4, 5]
match numbers:
	case [first, *middle, last]:
		print(first)
		print(middle)
 