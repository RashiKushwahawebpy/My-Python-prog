#26. Complex Real Example
response = {
 "status": 200,
 "data": ["apple", "banana"]
}
match response:
	case {"status": 200, "data": data}:
		print("Success:", data)
	case {"status": 404}:
		print("Not Found")
	case _:
		print("Unknown response") 