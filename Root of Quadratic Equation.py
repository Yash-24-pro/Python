import math
def roots_qe(a,b,c):
    disc = (b**2- 4*a*c)
    if disc == 0:
        root = -b/(2*a)
        print("Two Real and Equal roots Exists")
        print("root of quadratic equation is: ",root)
    elif disc >= 0:
        print("Two Real and Different roots Exists")
        root1 = (-b + math.sqrt(disc))/(2*a)
        root2 = (-b - math.sqrt(disc))/(2*a)
        print("root of quadratic equation are: ",root1, "and", root2 )
    else:
        real_part = -b / (2*a)
        print("Two Imaginary roots Exists")
        imaginary_part = math.sqrt(abs(disc)) / (2*a)
        print("roots of quadratic equation are: ", real_part,"+ i",imaginary_part)
        print("and ", real_part,"- i",imaginary_part)
a = int(input("Enter coeff. of x**2 : "))
b = int(input("Enter coeff. of x : "))
c = int(input("Enter constant : "))
roots_qe(a,b,c)
