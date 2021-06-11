def big_fibonacci(n):
    k=1
    f1=1
    f2=1
    f=1
    while(k<n):
        f=f1+f2
        f1=f2
        f2=f
        k=len(str(f))
    return f


print(big_fibonacci(1))
print(big_fibonacci(2))
print(big_fibonacci(3))
print(big_fibonacci(5))
print(big_fibonacci(30))