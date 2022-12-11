# Email slicer


n=input("\nWould you like to use email-slicer? (y/n) ")
print()
print()
if n=='y': 
    print("\nWELCOME TO EMAIL_SLICER! ")

    a=input("\nHow many emails would you like to slice? ")
    x=int(a)
    for i in range(1,x+1):
        email=input("Please input your email ")
        b=len(email)
        c=0
        for i in range (1,b):
            if email[i]=="@":
                c+=i
        if c>0:
            q=''
            for i in range (0,c):
                q+=email[i]
            e=''
            for i in range (c+1,b):
                e+=email[i]
            print(f'Your username is {q} and your domain is {e}')
        else:
            print('Invalid email adress given')
    print(' \n Thank you for visiting email-slicer, hope you visit us again! ')

else:
    print(' \n Thank you for visiting email-slicer, hope you visit us again! ')

    
