import random
n = random.randint(1,100)
a = -1
guess = 0
while(a != n):
    guess += 1
    a = int(input("Enter your guess:"))
    if(a < n):
        print("Go higher")
    elif(a>n):
        print("Go lower")
else:
    print(f"You guessed {n} in {guess} guesses")

