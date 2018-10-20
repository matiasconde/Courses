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

a = fib(10)
print(a)