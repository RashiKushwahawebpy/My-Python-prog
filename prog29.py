#11. Nested Pattern Matching
data = (1, [2, 3])
match data:
	case (1, [x, y]):
		print (x , y)