a,b,c=map(int,input().split())
d=(a+b+c)/2
e=(d*(d-a)*(d-b)*(d-c))**(0.5)
print(f"{e:.2f}")