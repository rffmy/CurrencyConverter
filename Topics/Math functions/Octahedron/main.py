import math

a = int(input())

area = round(2 * math.sqrt(3) * math.pow(a, 2), 2)
volume = round((1 / 3) * math.sqrt(2) * math.pow(a, 3), 2)

print(str(area) + " " + str(volume))
