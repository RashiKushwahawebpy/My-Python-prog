#20. Match String Patterns
text = "hello"
match text:
	case "hello":
		print("Greeting")
	case _:
		print("Other") 