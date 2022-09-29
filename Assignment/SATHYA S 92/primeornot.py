a=int(input("Enter Number:"))
c=0
for i in range(1,a+1):
    if a%i==0:
        c=c+1
if c>2:
    print("Not Prime")
elif c==2:
    print("Prime")