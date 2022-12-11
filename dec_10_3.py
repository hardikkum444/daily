# write a program to check if the given number is prime or not

# n=int(input("Enter any number "))
# for i in range (2,n):
#     if (n%i==0):
#         print('The given number is not prime')
#     else:
#         print("The given number is prime")

# see the problem in the above solution is that it will check the value for all the number from 
# 2 to n
# we dont want that, what we want is that we want to stop the entire process as soon as 1 facter
# is found so that it doesnt contine and all we get is one output

n=int(input('Enter any number '))
prime= True  
for i in range (2,n):
    if (n%i==0):
        prime= False
        break

if prime==True:
    print("Entered number is prime")

if prime==False:
    print("Entered number is not prime")

