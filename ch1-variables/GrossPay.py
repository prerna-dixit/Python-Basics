#PROJECT 3
#1-ask the user for the number of hours they work for
#2-ask the user, the rate per hour
#3-calculate the gross pay with a precision of 2 decimal places

hour = input("How many hours do you work for? \n")
rate = input("Enter the rate per hour: \n")
gross = round(float(hour)*float(rate), 2)
print(f"Gross Pay: {gross}")