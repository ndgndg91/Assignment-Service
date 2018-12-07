def ise(n):
    if n==0:
        return True
    else:
        return iso(n-1)

def iso(n):
    if n==0:
        return False
    else:
        return ise(n-1)

print(iso(3))
print(iso(2))
print(ise(3))
print(ise(2))

def fibo(n):
    # 재귀함수는 탈출조건이 꼭 필요하다.
    if n == 0 :
        return 0
    elif n == 1 or n==2:
        return 1
    return fibo(n-2) + fibo(n-1)

# index n까지의 피보나치 수열 구하기
def fibo_list(n):
    for i in range(n):
        print(fibo(i), end= " ")


fibo_list(8)
print()


def fibonach(n):
    if n == 1 :
        print(0)
    elif n==2:
        print(0,1)
    elif n>=3:
        a, b = 0, 1
        i =2
        while i <= n+1:
            # print(i,end=":")
            print(a,end=" ")
            a,b = b,a+b
            i+=1


fibonach(8)
