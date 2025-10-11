#•	Student Grade Calculator (Input student scores and return grades).
def gradeCalculator(user_marks, total_marks):
    percentage = (user_marks * 100) / total_marks
    if percentage >= 90:
        return "A++", percentage
    elif percentage >= 85 and percentage < 90:
        return "A+", percentage
    elif percentage >= 80 and percentage < 85:
        return "A", percentage
    elif percentage >= 75 and percentage < 80:
        return "B+", percentage
    elif percentage >= 70 and percentage < 75:
        return "B", percentage
    elif percentage >= 65 and percentage < 70:
        return "C+", percentage
    elif percentage >= 60 and percentage < 65:
        return "C", percentage
    elif percentage >= 55 and percentage < 60:
        return "D+", percentage
    elif percentage >= 50 and percentage < 55:
        return "D", percentage
    elif percentage >= 45 and percentage < 50:
        return "E+", percentage
    elif percentage >= 40 and percentage < 45:
        return "E", percentage
    else:
        return "F", percentage

user_marks, total_marks = map(int, input("Enter marks obtained and total marks ( Space seperated ): ").split())
grade, percentage = gradeCalculator(user_marks, total_marks)
print(f"Your grade is {grade} and percentage is {percentage:0.2f} according to your marks.")
