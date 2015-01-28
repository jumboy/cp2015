__author__ = 'jinya_000'

from math import pi
radius = float(input("Enter the radius in cm here:"))
length = float(input("Enter the length in cm here:"))

area = radius*radius*pi
volume = area*length
print("\n")

print("the volume is: " + str(volume))