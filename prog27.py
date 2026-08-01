#9. Using if Guard in Case
num = 15
match num:
	case x if x > 10:
		print("Greater than 10")
	case x:
		print("10 or less") 