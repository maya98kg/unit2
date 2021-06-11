
def is_prime(x):
    if(x<=1):
        return False
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return False
    return True
    
        

#print(is_prime(1))
#print(is_prime(17))
#print(is_prime(5))
#print(is_prime(12))