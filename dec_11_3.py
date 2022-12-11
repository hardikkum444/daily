# subtraction quiz loop

count=0
questions=5
i=0

while i<5:
    import random
    n1=random.randint(0,9)
    n2=random.randint(0,9)
    if n1<n2:
        n1,n2=n2,n2
    x=n1-n2    
    ans=int(input(f"What is {n1}-{n2}? "))
    if ans==x:
        count+=1
    else:
        count+=0

    i+=1

if count==1:
    print(f"You got 1 question right out of {questions}")
else:
    print(f'You got {count} questions right out of {questions} ')