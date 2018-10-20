import math

a,b=0,1
c=0
i=1
while b<100:
    print(b)
    a,b=b,a+b
    c=(((1+(5)**0.5)/2)**i-((1-(5)**0.5)/2)**i)/(5**0.2)
    i+=1
    print(c)
    print(i)

def fibo2(n):
    result = []

    a, b = 0, 1

    while a<n:
        result.append(a)
        a, b = b, a+b

    return result

c=int(input("ingrese n: "))

print(fibo2(c))

def fib(n):
    fib_list = []
    for _ in range(n+1):
        a=1
        if _<=1:
            fib_list.append(_)
        else:
            fib_list.append(fib_list[_-1]+fib_list[_-2])
    return fib_list

print(fib(40))

ab = fib(10)
print(ab)