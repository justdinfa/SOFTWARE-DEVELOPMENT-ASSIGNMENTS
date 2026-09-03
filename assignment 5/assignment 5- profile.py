name = input("Enter Student Name: ")
score = float(input("Enter Score: "))
if score >= 70:
    grade = "A"
    remark = "Excellent"
elif score >= 60:
    grade = "B"
    remark = "Very Good"
elif score >= 50:
    grade = "c"
    remark = "Good"
elif score >= 45:
    grade = "D"
    remark = "pass"
elif score > 40:
    grade = "E"
    remark = "pass"
elif score >= 0 and score < 40:
    grade = "F"
    remark = "Fail"


print("==========================")
print("STUDENT RESULT")
print("==========================")
print("Name:", name)
print("Score:", score)
print("Grade:", grade)
print("Remark:", remark)


if grade == "F":
    print("better luck next time")
else:
    print("Congratulations")