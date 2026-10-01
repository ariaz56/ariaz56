emp_id = input("Enter Employee ID: ")
emp_name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

hra = basic_salary * 0.20      # House Rent Allowance (20%)
da = basic_salary * 0.10       # Dearness Allowance (10%)
pf = basic_salary * 0.12       # Provident Fund (12%)

gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf

print("\n========== EMPLOYEE PAYROLL ==========")
print(f"Employee ID   : {emp_id}")
print(f"Employee Name : {emp_name}")
print(f"Basic Salary  : ₹{basic_salary:.2f}")
print(f"HRA (20%)     : ₹{hra:.2f}")
print(f"DA (10%)      : ₹{da:.2f}")
print(f"PF (12%)      : ₹{pf:.2f}")
print(f"Gross Salary  : ₹{gross_salary:.2f}")
print(f"Net Salary    : ₹{net_salary:.2f}")
print("======================================")