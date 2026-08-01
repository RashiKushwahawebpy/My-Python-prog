#Write a program to count vowels, consonants, digits, and special characters in a string.
text = input("Enter a string: ")

vowels = consonants = digits = special = 0

for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Special Characters =", special)
