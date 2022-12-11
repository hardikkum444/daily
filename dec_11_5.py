# conversion of while loop into for loop

# i = 0
# sum = 0 
# while sum<10000:
#     sum+=i
#     i+=1


sum=0
for i in range (0,10000):
    sum=sum+i

print(sum)


# conversion of for loop into while loop:

# sum=0
# for i in range(1001):
#     sum+=i

i=0 
sum=0
while i <1001:
    sum+=i
    i+=1
    
print(sum)