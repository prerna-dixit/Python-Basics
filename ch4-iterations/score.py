#highest score in the class
student_score=[80, 60, 55, 75, 65, 90]
highest=0
for scores in student_score:
    if scores>highest:
        highest=scores
print(f"highest score is: {highest}")