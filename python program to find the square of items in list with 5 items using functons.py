list = []
n = int(input("enter the number of items in list: "))
for i in range(n+1):
    item = input("Enter item:")
    list.append(item)
print(list)


def square_items(input_list):
    return [x ** 2 for x in input_list]

numbers = []

print("Enter 5 numbers:")
for _ in range(5):
    number = int(input())
    numbers.append(number)

squared_numbers = square_items(numbers)

# Output the result
print("Original list:", numbers)
print("List of squares:", squared_numbers)


# method 2 
def square_items(input_list):
    return [x ** 2 for x in input_list]

numbers = []

print("Enter 5 numbers: ")
for _ in range(5):
    number = int(input())
    numbers.append(number)

squared_numbers = square_items(numbers)

# Output the result
print("Original list:", numbers)
print("List of squares:", squared_numbers)