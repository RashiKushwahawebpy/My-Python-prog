#7. Dictionary Pattern Matching
person = {"name": "Manish", "age": 30}
match person:
	case {"name": name, "age": age}:
		print(name, age) 
