#3.6 Optional Practice
# Create check_guess()
# Call with test
def check_guess(letter, guess):
    guess_test = False
    if guess.isalpha() == False:
        print('Invalid guess')
    elif guess > letter:
        print('Guess is high')
    elif guess < letter:
        print('Guess is low')
    else:
        guess_test = True
    return guess_test
def letter_guess(letter_to_guess):
    user_letter = input('Guess a single letter of the alphabet (attempt 1 of 3): ').lower()
    correct_guess = check_guess(letter_to_guess, user_letter)
    if correct_guess == True:
        pass
    else:
        user_letter = input('Guess a single letter of the alphabet (attempt 2 of 3): ').lower()
        correct_guess = check_guess(letter_to_guess, user_letter)
        if correct_guess == True:
            pass
        else:    
            user_letter = input('Guess a single letter of the alphabet (attempt 3 of 3): ').lower()
            correct_guess = check_guess(letter_to_guess, user_letter)
    return correct_guess
guess_result = letter_guess('q')
if guess_result == True:
    print('Guess is correct!')
else:
    print('Thanks for playing.')