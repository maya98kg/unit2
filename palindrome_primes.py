def palindrome_primes():
    result=[]
    for i in range(10000,100000):
        if is_prime(i) and palindrome(i):
            result.append(i)
    return result

def is_prime(x):
    if(x<=1):
        return False
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return False
    return True

def palindrome(n):
    first_half=n//1000
    second_half=10*(n%10)+((n//10)%10)
    if(first_half==second_half):
        return True
    else:
        return False

#print(palindrome_primes())