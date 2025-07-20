#PROJECT 7
#takes a year as an input and checks if the year is leap year or not

year=int(input("Enter a year- "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"It is a leap year.")
        else:
            print(f"Not a leap year.")
    else:
        print(f"It is a leap year.")
else:
    print(f"Not a leap year.")