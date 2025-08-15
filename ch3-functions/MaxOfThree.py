#PROJECT 14 
#Finds the max of three numbers

def maximum(a, b, c):
    if a>b:
        max = a
    else:
        max = b

    if max>c:
        print(f"{max} is the maximum.")
    else:
        print(f"{c} is the maximum.")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
maximum(a, b, c)
