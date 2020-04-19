import random


def check_guesses(guess_limit, number_of_guesses):
    secret_number = random.randint(1, guess_limit)

    while number_of_guesses > 0:
        number_of_guesses -= 1

        try:
            guess = int(input(f'Guess a number between 1 and {guess_limit}: '))
            
            if guess == secret_number:
                print('You got it right!')
                break
            elif guess > guess_limit:
                print('Number is too large. Please, enter number within range!')
                number_of_guesses += 1
            else:
                print('That was wrong!')
                if number_of_guesses == 1:
                    print(f'You have {number_of_guesses} guess left!')
                else:
                    print(f'You have {number_of_guesses} guesses left!')

        except ValueError:
            print('Please, enter only numbers!')
            number_of_guesses += 1

    if number_of_guesses == 0 and guess != secret_number:
        print('Game Over!')


print('''
Choose Your Level!
    * Enter 1 for Easy
    * Enter 2 for Medium
    * Enter 3 for Hard
''')
level = input('Level: ')
number_of_guesses = 0
guess = 0
secret_number = 0

if level == '1':
    check_guesses(10, 6)

if level == '2':
    check_guesses(20, 4)

if level == '3':
    check_guesses(50, 3)
    