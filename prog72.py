numbers = list(map(int, input("Enter Numbers: ").split()))
positive = negative = zero = 0
for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1
print("Positive Numbers :", positive)
print("Negative Numbers :", negative)
print("Zero :", zero)