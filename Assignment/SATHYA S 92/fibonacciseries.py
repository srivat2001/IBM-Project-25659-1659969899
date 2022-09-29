l=int(input("limit:"))
a=0
b=1
print("\n",a)
print(",\n",b)
for i in range(0,l):
    a = a + b
    print(",\n",a)
    b = b + a
    print(",\n",b)

