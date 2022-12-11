# sentinel value question 

number=0
gameover=False

while gameover==False:
    n=int(input("Enter a number (the input will end if you input 0) "))
    if n==0:
        gameover=True
        print(f"The sum is {number}")
    else:
        number+=n
    


