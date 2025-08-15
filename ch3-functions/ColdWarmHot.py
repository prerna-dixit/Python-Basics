#PROJECT 13
#define a function that takes temperature as a parameter
#returns hot if temp>28, warm if temp bw 18 and 28 including both AND cold if less than 18C

def temperature(temp):
    if temp>28:
        print(f"Hot!!")
    elif temp<18:
        print("Cold~")
    else:
        print("Warm!")

temp=float(input("Enter temperature: "))
temperature(temp)