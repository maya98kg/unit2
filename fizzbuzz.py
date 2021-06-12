def fizzbuzz(n):
    if(n%3==0) and (n%5==0):
        print("FizzBuzz")
    elif(n%3==0):
        print("Fizz")
    elif(n%5==0):
        print("Buzz")
    if (n%3!=0) or (n%5!=0):
        print(n)

for n in range(1,1001):
    fizzbuzz(n)