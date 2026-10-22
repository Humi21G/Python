def calculateGrade(mark):
    if mark >= 75:
        return "Distinction"
    elif mark >= 50:
        return "Pass"
    else:
        return "Fail"


name = input("Enter the student's name: ")
mark = int(input("Enter the student's mark: "))

if mark >= 0 and mark <= 100:
    grade = calculateGrade(mark)
    print(f"{name}, your grade is: {grade}")
else:
    print("Invalid mark. Please enter a value between 0 and 100.")