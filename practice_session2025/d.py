from math import sqrt, pi

c_area = int(input())  # c_area = c_radius**2 * pi → c_radius = sqrt(c_area/pi)
c_radius = sqrt(c_area / pi)

s_side = 2 * c_radius + 2

print(s_side ** 2)
