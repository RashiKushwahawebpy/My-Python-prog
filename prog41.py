#24. Combining Patterns
data = [1, 2, 3]
match data:
	case [1, *rest]:
		print(rest)