#wap to find the largest number of n inputs

n=int(input("how many number you want to enter : "))
i=1
larg=int(input("enter a number :"))
while(i<n):
  n1=int(input("enter a number :"))
  if (n1 > larg):
    larg=n1
  i+=1
print("largest mnumber",larg)
