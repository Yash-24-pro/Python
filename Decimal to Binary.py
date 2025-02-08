def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary  # Add remainder to binary string
        n //= 2  # Perform integer division by 2
    return binary

# Input decimal number from the user
num = int(input("Enter a decimal number: "))

# Convert to binary
binary_result = decimal_to_binary(num)

# Output the binary equivalent
print("The binary equivalent of ",num," is: ", binary_result)