def sum_of_digits(number):
   sum = 0
   while number>0:
      sum += number%10
      number//=10
   return(sum)
num = int(input("Enter the number: "))
total = sum_of_digits(num)
print("sum of digits: ",total)




    
