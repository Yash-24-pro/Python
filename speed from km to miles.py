#Using formula
speed = float(input("enter the speed in km/hr: "))
speed_miles = speed * 0.0621
print("speed in miles/hr:",speed_miles,"miles/hr")

#using function
def km_miles(a):
    speed_miles = a * 0.0621
    print("speed in miles/hr: ",speed_miles)
    return speed_miles 
kmph_speed = float(input("Enter speed in km/hr: "))
                
km_miles(kmph_speed)