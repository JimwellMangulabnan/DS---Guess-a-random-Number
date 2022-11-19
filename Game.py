import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time! ")
        quit()
else: 
    print("please type a Number next time! ")
    quit()

random_number = random.randint(0, top_of_range)
guesess = 0

while True:
    guesess += 1
    try:
        user_guess = int(input("Make a Guess"))
    except ValueError:
        print("Please type a number!!!")
        continue
    else:
        if user_guess == random_number:
            print("Yey! you got it!")
            break
        elif user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

print("You got it in ", guesess, "guesses!!!")


