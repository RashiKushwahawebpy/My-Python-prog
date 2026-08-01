marks = {}
for i in range(5):
    subject = input("Enter Subject Name: ")
    score = int(input("Enter Marks: "))
    marks[subject] = score
    total = sum(marks.values())
    percentage = total / 5
    print("\nSubject Marks")
for subject, score in marks.items():
    print(subject, ":", score)
    print("Total =", total)
    print("Percentage =", percentage) 
