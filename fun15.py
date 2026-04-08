def sum(n):
    t=0
    for i in range(1,n+1):
        t=t+i
    return t
n=int(input("enter a number: "))
r=sum(n)
print(r)