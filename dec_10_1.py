list=[1,2,1,2,5]
list2=[]
for i in list:
    if list.count(i)==1:
        list2.append(i)

print(list2) 