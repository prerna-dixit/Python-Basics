#PROJECT 5
#1-Greet the user
#2-input no of days, hotel price, flight price, rental car price, other expenses
#3-calculate the total cost with 2 decimal precision

print("Welcome to Trip Cost Calculator~ ")
days = int (input("How many days will you stay for?"))
hotel = float (input("How much does the hotel cost per day?"))
flight = float (input("How much does the flight fare cost?"))
car = float (input("How much does the rental car cost per day?"))
other = float(input("Any other expenses? "))
total = float(round((hotel*days)+(flight)+(car*days)+other, 2))
print(f"Here's your total cost for the trip: {total} ")
percent = float (input("How much percent tax is applied on the bill? "))
tax = (percent*0.01*total)+total
print(f"Total cost including taxes: {tax} ")
