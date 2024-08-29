import math
print("Area of circle with radius 5: " + str(math.pi * (5**2)))
print("Volume of sphere with radius 3: " + str(3**3 * 4.0/3.0 * math.pi))
print("Hypotenuse of right-angled triangle with sides 3 and 4: " + str(math.sqrt((3**2) + (4**2))))

myName = "Caleb Alexander Brown"
print(len(myName))
print ("Caleb" + " " + "Brown")
print(myName.upper())
print(myName.lower())

age = 19
height = 5 #I think
weight = math.nan

print("age: " + str(type(age)))
print("height: " + str(type(height)))
print("weight: " + str(type(weight)))

bmi = ((weight/height*12) ** 2 )*703
print("bmi: " + str(bmi))