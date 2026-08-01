#Write a function to check whether two strings are anagrams. 
def anagram(str1, str2):
	if sorted(str1) == sorted(str2):
		print("Anagram")
	else:
		print("Not Anagram")
s1 = input("Enter First String: ")
s2 = input("Enter Second String: ") 