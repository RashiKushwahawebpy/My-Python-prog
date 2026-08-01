#18. Capture Remaining Items
items = [1, 2, 3, 4]
match items:
	case [first, *rest]:
		print(first)
		print(rest) 
