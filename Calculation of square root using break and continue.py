import math 

while True:
   n = (input("Enter a number or type exit to quit : "))
   if n.lower() == "exit" :
      print("Exiting")
      break
   a = int(n)
   if a <= 0:
      print("cannot calculate the square root")
      continue
   else:
      print("square root of", n ,"is:",math.sqrt(a))