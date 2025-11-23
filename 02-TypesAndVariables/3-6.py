import math
height_m =input('Podaj swój wzrost(m):')
height_m =float(height_m)
distance_km = 3,57 * math.sqrt(height_m)
print('Odległość od ciebie do horyzontu:', distance_km)