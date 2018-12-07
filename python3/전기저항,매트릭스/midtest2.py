from math import sqrt

total_1 = 0  # sum
total_2 = 0  # x^2
count = 0
value = 0

while value != -1 : 
    value = float(input("Enter floating-point data : "))

    if(value != -1) :
        total_1 += value
        total_2 += value * value
        count += 1

ave = (total_1/count)   # average value
s = sqrt((total_2-(1/count)*total_1**2)/(count-1))


print()
print('Average is %.2f' %ave)
print('Standard deviation is %.2f' %s)