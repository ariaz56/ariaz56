# Train Ticket Reservation System

name = input("Enter Passenger Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender(in M/F):")
train_name = input("Enter Train Name: ")
source = input("From: ")
destination = input("To: ")
distance = float(input("Enter Distance (in km): "))

price_per_km = 5
price = distance * price_per_km

if age >= 60:
    price = price * 0.80

print("\n========== TRAIN TICKET ==========")
print("Passenger Name :", name)
print("Age            :", age)
print("Gender (M/F)   :",gender)
print("Train Name     :", train_name)
print("From           :", source)
print("To             :", destination)
print("Distance       :", distance, "km")
print("Ticket Price   : ₹", price)
print("==================================")
print("Thank You! Happy Journey!!")
print("==================================")