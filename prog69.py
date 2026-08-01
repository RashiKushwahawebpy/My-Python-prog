numbers = list(map(int, input("Enter Numbers: ").split()))
unique = []
for item in numbers:
 if item not in unique:
    unique.append(item)
print("Original List :", numbers)
print("List after removing duplicates :", unique) 