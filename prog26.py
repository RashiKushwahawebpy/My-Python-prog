#8. Partial Dictionary Matching
data = {"name": "Ram", "age": 25, "city": "Lucknow"}
match data:
	case {"name": name}:
		print(name) 
