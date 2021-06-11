def primes_below(n):
    result=[]
    for i in range(2,n):
        if(is_prime(i)):
            result.append(i)
    return result


def is_prime(x):
    if(x<=1):
        return False
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return False
    return True