#PROJECT 10
#enters gpa frm the user n tells the grade
# grade- >=9 O
# >=8 A+
# >=7 A
# >=6 B
# >=5 C
# >=4 D
# >=3.3 GRACE
# <3.3 F

gpa = input("Enter your GPA out of 10: ")
try:
    gpa=float(gpa)
except ValueError:
    print("Not a valid input! ")
    quit()

if gpa<=10.0 and gpa>=9.0:
    print(f"Outstanding~ O")
elif gpa<9.0 and gpa>=8.0:
    print(f"A+")
elif gpa<8.0 and gpa>=7.0:
    print(f"A")
elif gpa<7.0 and gpa>=6.0:
    print(f"B")
elif gpa<6.0 and gpa>=5.0:
    print(f"C")
elif gpa<5.0 and gpa>=4.0:
    print(f"D")
elif gpa<4.0 and gpa>=3.3:
    print("GRACE")
else:
    print("Failed~ F")
