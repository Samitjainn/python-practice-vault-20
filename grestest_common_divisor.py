a=int(input("enter first number"))
b=int(input("enter second number"))
while (b!=0):
      rem=a%b
      a=b
      b=rem
print("greatest common divisor",a)
