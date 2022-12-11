# guessing number game

import random 

n1=random.randint(1,100)
gameover =False 

guess=int(input("Guess a number between 1 and 100 "))
number=0

if guess==n1:
    print("You have guessed the number correctly in 1 go! ")
    gameover=True


while not gameover:
    if guess<n1:
        guess=int(input("Too low, guess again "))
        number+=1
    
    if guess>n1:
        guess=int(input("Too high, guess again "))
        number+=1
        
    if guess==n1:
        print(f"You guessed the number in {number} times ")
        gameover=True

    

        