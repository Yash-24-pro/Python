def add_binary(bin1, bin2):
# Convert binary strings to integers
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    sum_num = num1 + num2
    
 # Convert the sum back to binary and return (remove '0b' prefix)
    return bin(sum_num)[2:]

# Input two binary numbers
binary1 = input("Enter the first binary number: ")
binary2 = input("Enter the second binary number: ")

# Add the binary numbers
result = add_binary(binary1, binary2)

# Display the result
print("The sum of {binary1} and {binary2} is: {result}")
