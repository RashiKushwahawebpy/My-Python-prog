#4. Tuple Pattern Matching
data = (1, 2)
match data:
	case (1, 2):
		print("Matched tuple")
	case (x, y):
		print(x, y)