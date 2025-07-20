#PROJECT 9
#Rewrite gross pay program using try n except so that the program handles non numeric inputs by printing a message n exiting the program [print an error message or something]
#quit() function exits a program
#print "enter a numericd value please" for a valueerror

hours = int(input("How many hours do you work for in a week? "))
try:
    hours=float(hours)
except ValueError:
    print("ERROR! Please enter numeric value for hour.")
    quit()
    
rate = int(input("What's the hourly rate that you work on? "))
try:
    rate=float(rate)
except ValueError:
    print("ERROR! Please enter numeric value for rate.")
    quit()

if hours>40:
    overtime = hours-40
    extraPay = 1.5*rate*overtime
    grossPay = round((rate*40)+extraPay, 2)
else:
    grossPay=round(hours*rate, 2)
print(f"Gross Pay = {grossPay}")


