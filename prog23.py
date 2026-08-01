#5. List Pattern Matching
numbers = [1, 2, 3]
match numbers:
	case [1, 2, 3]:
		print("Exact match")
	case [x, y, z]:
		print(x, y, z)