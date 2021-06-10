from math import sqrt
def solve_quadratic(a,b,c):
    if (b*b-4*a*c>0):
        x1=(-b+sqrt(b*b-4*a*c))/(2*a)
        x2=(-b-sqrt(b*b-4*a*c))/(2*a)
        return (x1,x2)
    elif (b*b-4*a*c==0):
        x=(-b)/(2*a)
        return x