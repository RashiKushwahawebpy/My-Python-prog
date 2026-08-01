#Input the user's name
name = input ("Enter your name: ")
vowels = "aeiou"
vowel_count = 0
for char in name.lower():
    if char in vowels:
        vowel_count +=1
        print(f"the number of vowels in '{name}' is:{vowel_count}")
        