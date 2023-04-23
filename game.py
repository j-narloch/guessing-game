correct_number = 7
guess_count = 0
guess_limit = 3


while guess_count < guess_limit:
    guess = int(input("Guess a number: "))
    guess_count += 1
    if guess == correct_number:
        print("Congratulations, you won!")
        break
else:
    print("Sorry, try again!")
