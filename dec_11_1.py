# Repeat sunbtraction quiz

import random

n1=random.randint(0,9)
n2=random.randint(0,9)

gameover =False

if n1<n2:
    n1,n2=n2,n1

a=(n1-n2)

answer=int(input(f'What is {n1}-{n2}? '))

if answer==a:
    print("you have got it! ")
    gameover=True
    
else:
     while not gameover:
        if answer!=a:
            print("You got it wrong.")
            answer=int(input(f'What is {n1}-{n2}? '))

        if answer==a:
            gameover=True
            print("Youhave got it! ")

       