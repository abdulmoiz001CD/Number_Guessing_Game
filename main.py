import random

print("welcome to the number guessing Game \n You got 5 chances to attempt the right number \n between 50 to 100")


number_to_guess = random.randrange(50,100)

chances:int = 5

user_take_chanc = 0

while user_take_chanc < chances :
    user_take_chanc += 1
    my_guess = int(input("Please enter Your number : "))

    if my_guess == number_to_guess:
        print(f"Hurrah You win the win the game by chosing {number_to_guess} in {user_take_chanc} attempt")
        break
    elif user_take_chanc >= chances and my_guess != number_to_guess :
        print("Hoo soory Better luck next time")

    elif my_guess < number_to_guess :
        print("Your guess is less than the actual number! Try Again")
    
    elif my_guess > number_to_guess :
        print("Your guess is greater than the actual number! Try Again")