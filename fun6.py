def calculate(n):
    if n<0:
        return  "not exist"
    elif n == 0:
        return 1
    else:
        c=1
        for i in range(1,n+1):
            c=c*i
        return c
n=int(input("enter a number: "))
r=calculate(n)
print("the factorial is:",r)