#B Write a program to create a text file and store student names you want. 
Ans= True 
f1= open("stu.txt","w") 
while Ans: 
    str= input("Enter friend name:") 
    f1.write(str) 
    Ans= input("Do you want to continue enter Yes otherwise press enter") 
f1.close() 
print("Data store Successfully. To check Open in note pad")
print("Bye!Bye!") 