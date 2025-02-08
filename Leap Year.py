a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print("Leap years are: ")
for year in range(a,b+1):
    if(year%4 == 0 and year % 100!=0) or ( year % 400 == 0):
        print(year, end = ' ')