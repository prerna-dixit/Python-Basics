#PROJECT 6
#if working hours are above 40, pay 1.5 times hourly rate for the overtime
rate = int(input("What's the hourly rate that you work on? "))
hours = int(input("How many hours do you work for in a week? "))
if hours>40:
    overtime = hours-40
    extraPay = 1.5*rate*overtime
    grossPay = round((rate*40)+extraPay, 2)
else:
    grossPay=round(hours*rate, 2)
print(f"Gross Pay = {grossPay}")


