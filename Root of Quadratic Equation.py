"""Finds the roots of a quadratic equation ax^2 + bx + c = 0"""

import math

def quadratic_roots(a, b, c):
    
    if a == 0:
        return "Coefficient 'a' cannot be zero. This is not a quadratic equation."
    
    disc = b**2 - 4*a*c  # Discriminant
    
    if disc == 0:
        root = -b / (2 * a)
        return f"Two Real and Equal roots exist: {root}"

    elif disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2 * a)
        root2 = (-b - math.sqrt(disc)) / (2 * a)
        return f"Two Real and Different roots exist: {root1} and {root2}"

    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(disc)) / (2 * a)
        return (f"Two Imaginary roots exist: {real_part} + {imaginary_part}i "
                f"and {real_part} - {imaginary_part}i")

try:
    a = float(input("Enter coefficient of x^2: "))
    b = float(input("Enter coefficient of x: "))
    c = float(input("Enter constant: "))
    print(quadratic_roots(a, b, c))

except ValueError:
    print("Invalid input! Please enter numeric values.")
