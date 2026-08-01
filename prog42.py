#25. Match with Alias (as keyword)
data = [1, 2, 3]
match data:
	case [1, 2, 3] as fulllist:
		print(fulllist)