import math


def diameter(wireGauge):
    return 0.127 * pow(92, ((36 - wireGauge) / 39))


def copperWireResistance(length, wireGauge):
    d = diameter(wireGauge)
    A = math.pi * d * d
    L = length
    return round(4 * ((1.678 * pow(10, -8)) * L) / A, 4)


def aluminumWireResistance(length, wireGauge):
    d = diameter(wireGauge)
    A = math.pi * d * d
    L = length
    return round(4 * ((2.82 * pow(10, -8)) * L) / A, 4)


n = int(input('Enter n (wire gauge):'))
L = int(input('Enter L (length):'))
copper = copperWireResistance(L, n)
aluminum = aluminumWireResistance(L, n)
print('The resistance of copper wire is', copper)
print('The resistance of aluminum wire is', aluminum)




