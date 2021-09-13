#Student ID: 1201201695
#Student Name: Peong Khay Zhien

import math

radius = float(input("Enter radius: "))
surface = 4 * math.pi * (radius * radius)
volume = 4/3 * math.pi *  (radius * radius * radius)
print("Surface area of sphere is {:.2f}".format(surface))
print("Volume of sphere is {:.2f}".format(volume))