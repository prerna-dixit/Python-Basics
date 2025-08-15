def validate_float(value):
    try:
        return float(value)
    except ValueError:
        print("ERROR, ENTER A VALID INPUT")
        exit()  # stop the program if invalid


def GrossPayOvertime(hours, rate):
    if hours > 40:
        overtime = hours - 40
        extraPay = 1.5 * rate * overtime
        grossPay = round((rate * 40) + extraPay, 2)
    else:
        grossPay = round(hours * rate, 2)
    print(f"Gross Pay = {grossPay}")


# Get validated inputs
hours = validate_float(input("Enter the number of hours: "))
rate = validate_float(input("Enter the hourly rate: "))

GrossPayOvertime(hours, rate)
