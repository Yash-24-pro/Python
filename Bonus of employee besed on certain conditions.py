#  A company decides to give bonus to all employees on Diwali. A 5% bonus on salary is given to the male workers and 10% bonus on salary to the female workers. 
# Write a program to enter the salary of the employee and sex of the employee. Calculate the bonus of the employee. (Hint:if-else)

salary = int(input("Enter the salary of the employee : "))
sex = input("Enter the sex of the employee : ")
if sex == "M" or "Male":
    print("The Bonus is: ",0.05*salary,"rs")
else:
    print("The Bonus is: ",0.1*salary,"rs")