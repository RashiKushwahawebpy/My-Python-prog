#16. Wildcard _ Pattern
command = "start"
match command:
	case "run":
		print("Running")
	case _:
		print("Unknown command")