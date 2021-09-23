# Author: JD 09/23/2021

radius = int(input("Please enter the radius: "))

height = int(input("Please enter the height: "))

pi = 3.14

volume = pi * (radius ** 2) * height

surface_area = 2 * pi * radius * (height + radius)

print(volume)

print(surface_area)