#use of user defined function and docstrings
#calculator
def calculator(num1, num2, operator):
    """calculator that inputs two operands and an operator and performs the operation"""
    if operator == "+":
        result=num1+num2
        print(f"{num1}+{num2}={result}")
    elif operator == "-":
        result=num1-num2
        print(f"{num1}-{num2}={result}")
    elif operator == "*":
        result=num1*num2
        print(f"{num1}*{num2}={result}")
    elif operator == "/":
        result = num1/num2
        print(f"{num1}/{num2}={result}")
    else:
        return f"Enter a valid operator"
num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))
operator = input("Pick operation from this list (+,-,*,/) ")    
calculator(num1, num2, operator)