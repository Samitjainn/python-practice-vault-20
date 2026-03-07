# Program to reverse a number
# Example: if n = 1234, output should be 4321

n=int(input("enter a number you want to reverse :"))
rev=0
while(n>0):
   # Extract the last digit
  digit=n%10
  # Add digit to reversed number
  rev=rev*10+digit
  # Remove last digit from number
  n= n //10
print("reversed number :",rev)  
