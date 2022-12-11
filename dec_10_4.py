# program to write factorial of a number using loops:

n=int(input("Enter any number "))
total=1
for i in range (1,(n+1)):
    total*=i
print(total)