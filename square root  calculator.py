import math

print("Square Root Calculator")
print("Enter a number to calculate its square root or Enter 999 to exit the program..")
while True:
    try:
        number = float(input("Enter a number: "))
        
        
        # Break if the user enters 999
        if number == 999:
            print("Exiting the program. Goodbye!")
            break
        
        # Skip negative numbers
        elif number < 0:
            print("Negative numbers don't have real square roots. Try again!")
            continue
        
        # Calculate and display the square root
        square_root = math.sqrt(number)
        print("The square root of ",number," is:",square_root)
    
    except ValueError:
        # Handle invalid inputs that aren't numbers
        print("Invalid input! Please enter a valid number.")
