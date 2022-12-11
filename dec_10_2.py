# program to greet the person whose name starts with 'h' inside the list


list=['Hardik','Jacob','George','Jake']
for i in list:
    if i[0]=='H':
        print(f'Good morning {i}')


# or


for i in list:
    if i.startswith('H'):
        print(f'Good Morning {i}')