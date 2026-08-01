#Write a Python program to count vowels, consonants, digits, and special characters in a string.
text = input("Enter String: ")
vowel = consonant = digit = special = 0
for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowel += 1
        else:
            consonant += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1
print("Vowels =", vowel)
print("Consonants =", consonant)
print("Digits =", digit)
print("Special Characters =", special) 