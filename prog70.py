numbers = list(map(int, input("Enter Numbers: ").split()))
even = []
odd = []
for num in numbers:
 if num % 2 == 0:
    even.append(num)
 else:
    odd.append(num)
print("Even List :", even)
print("Odd List :", odd) 