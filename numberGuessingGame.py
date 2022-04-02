import random
print("Number Guessing Game")
chances=0
number=random.randint(1,9)
while chances < 5:
    guess = int(input("Guess A Number Between 1 and 9: "))
    if guess == number:
        print("YOU WON!!!")
        break
    elif guess < number:
        print("Your Guess Is Too Low!")
    else:
        print("Your Guess Is Too High")
    chances += 1
if not chances < 5:
    print("YOU LOSE!!! The Number Is", number)