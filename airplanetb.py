flights = {
    "AI101": {"route": "Chennai to Delhi", "price": 5500, "seats": 20},
    "AI102": {"route": "Chennai to Mumbai", "price": 4800, "seats": 15},
    "AI103": {"route": "Chennai to Bangalore", "price": 3000, "seats": 25}
}

print("========== AIRPLANE TICKET BOOKING ==========")

name = input("Enter Passenger Name: ")

print("\nAvailable Flights")
for code, details in flights.items():
    print(f"{code} - {details['route']} | Price: ₹{details['price']} | Seats: {details['seats']}")

flight_code = input("\nEnter Flight Code: ").upper()

if flight_code in flights:
    ticket_count = int(input("Enter Number of Tickets: "))

    if ticket_count <= flights[flight_code]["seats"]:
        total = ticket_count * flights[flight_code]["price"]
        flights[flight_code]["seats"] -= ticket_count

        print("\n========= BOOKING CONFIRMED =========")
        print("Passenger Name :", name)
        print("Flight Code    :", flight_code)
        print("Route          :", flights[flight_code]["route"])
        print("Tickets        :", ticket_count)
        print("Total Amount   : ₹", total)
        print("Status         : Confirmed")
        print("====================================")
    else:
        print("Sorry! Not enough seats available.")
else:
    print("Invalid Flight Code.")