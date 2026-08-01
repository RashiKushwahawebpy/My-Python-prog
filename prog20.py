#2. Multiple Values in One Case (| operator)
letter = "a" 
match letter:
	case "a" | "e" | "i" | "o" | "u":
		print("Vowel")
	case _:
		print("Consonant") 