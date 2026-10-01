# Electricity Bill Calculator

print("===== Electricity Bill Calculator =====")

name = input("Enter Customer Name: ")
units = float(input("Enter Units Consumed: "))

# Bill Calculation
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.5)
elif units <= 300:
    bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)
else:
    bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + ((units - 300) * 6)
   
# Fixed Charge
fixed_charge = 100
total_bill = bill + fixed_charge

# Output
print("\n========== ELECTRICITY BILL ==========")
print("Customer Name :", name)
print("Units Consumed:", units)
print("Energy Charge : ₹", round(bill, 2))
print("Fixed Charge  : ₹", fixed_charge)
print("Total Bill    : ₹", round(total_bill, 2))
print("======================================")