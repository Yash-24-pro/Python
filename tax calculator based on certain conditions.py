# Write a Program to calculate income tax to be paid by the
# employee of an organization


salary = float(input("Enter your salary: "))
taxable_income = salary - 250000  # Standard deduction
if taxable_income <= 0:
    print("No Tax to be paid")
else:
    if taxable_income <= 500000:
        tax = taxable_income * 0.05

    elif taxable_income <= 1000000:
        tax = 12500 + (taxable_income - 500000) * 0.2

    else:
        tax = 12500 + 100000 + (taxable_income - 1000000) * 0.3
    print("Tax to be paid :", tax ,"Rs")