import random

print("세 개의 양의 정수를 입력하시오: ")
number = 'num1', 'num2', 'num3'
num1 = int(input("첫번째 수: "))
num2 = int(input("두번째 수: "))
num3 = int(input("세번째 수: "))

sum = num1+num2+num3

if (sum%2) == 0:
        if num1 <= num2:
                if num2 <= num3:
                        print("max = num3")
                else :
                        print("max = num2")
        else:
                if num1<= num3:
                        print("max = num3")
                else:
                        print("max = num1")
elif num1 == num2 == num3 :
        print(random.choice(number))
else :
        print(sum)
