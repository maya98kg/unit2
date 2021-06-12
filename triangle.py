from math import sqrt
class Triangle():
    def __init__(self,x,y,z):
        self.a=x
        self.b=y
        self.c=z
    def perimeter(self):
        return (self.a+self.b+self.c)

    def area(self):
        s=(self.a+self.b+self.c)
        return sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

    def scale(self,scale_factor):
        return Triangle(scale_factor*self.a,scale_factor*self.b,scale_factor*self.c)
    
    def is_valid(self):
        if(self.a<self.b+self.c) and (self.b<self.a+self.c) and (self.c<self.b+self.a):
            return True
        else:
            return False
    def is_right(self):
        if(self.a*self.a==self.b*self.b+self.c*self.c) or (self.b*self.b==self.a*self.a+self.c*self.c) or (self.c*self.c==self.b*self.b+self.a*self.a):
            return True
        else:
            return False

#t=Triangle(3,4,5)
#t1=t.scale(3)
#print(t1.a)