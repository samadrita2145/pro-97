import random
print("Number guessing game")
number=random.randint(1,9)
chances=0
while chances<5: 
    guess= int(input("Enter your guess= "))
    if guess==number:
        print("Congradulations you won")
        break
    elif guess<number:
        print("Your guess is too low, guess a number higher than this")
    else: 
        print("Your guess is too higher, guess a number lower than this")
    chances+=1 
if not chances<5:
    print("You loose")