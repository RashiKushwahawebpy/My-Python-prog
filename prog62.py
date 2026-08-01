#Write a program using nested loops to print the following pattern upto no of lines input by user 
n = int(input("enter no of lines: "))
for i in range(1, n + 1):
	for j in range(1, i + 1):
		print(i * j, end=" ")
	print() 
