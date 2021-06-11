def my_reverse(l):
    n=len(l)
    new_l=[]
    while(n>0):
        n=n-1
        new_l.append(l[n])
    return(new_l)


print(my_reverse([1,2,3,4,5]))