students = int(input("Enter the number of students: "))
print("\n")
name = []
score = []
while students>0:
    name.append(str(input("Enter name here: ")))
    score.append(int(input("Enter score here: ")))
    print("\n")
    students -= 1
highest = max(score)
print("The student with the highest score is: ", name[score.index(highest)], "with a score: ", highest)
name.pop(score.index(highest))
score.pop(score.index(highest))
highest2 = max(score)
print("The student with the second highest score is: ", name[score.index(highest2)], "with a score: ", highest2)
