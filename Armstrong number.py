def is_armstrong_number(number):
    # Convert the number to a string to calculate the number of digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of the digits raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    return sum_of_powers == number

number = int(input("Enter a number: "))

if is_armstrong_number(number):
    print("number is an Armstrong number.")
else:
    print("number is not an Armstrong number.")
    
