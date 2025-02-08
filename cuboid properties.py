def cuboid_prop(l,b,h):
    volume = l*b*h
    print("Volume: ",volume)
    surface_area = 2*(l*b + b*h +h*l)
    print("Surface area: ",surface_area)
    space_diagonal = (l*l + b*b + h*h)**0.5
    print("length of Space Diagonal: 0",space_diagonal)

l = float(input("Enter length of cuboid: "))
b = float(input("Enter width of cuboid: "))
h = float(input("Enter height of cuboid: "))
cuboid_prop(l,b,h)