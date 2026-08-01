#15. Sequence Matching
data = [1, 2]
match data:
	case [x, y]:
		print("Two items")
	case [x, y, z]:
		print("Three items")