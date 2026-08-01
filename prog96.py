#Write a program to count the frequency of each character
text = input("Enter a string: ")
 
visited = ""
 
for ch in text:
	if ch not in visited:
    	    print(ch, "=", text.count(ch))
visited += ch
