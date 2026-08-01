#Write a program using loops to display the following pattern. 
for i in range(5):
	ch = chr(65 + i)
	for j in range(i + 1):
		print(ch, end= " ")
		print() 