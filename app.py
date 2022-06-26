# NOTE: Developed and tested using Python 3.10
import random

# Initialize variables
play_game = 'y'
number_range_low = 1
number_range_high = 10
high_score = 0


def get_random_int():
    """
    Returns a random integer between number_range_low and number_range_high
    """
    return random.randint(number_range_low, number_range_high)


while play_game.lower() == 'y':
    # Show welcome banner with intro message
    print('')
    print('/' * 79)
    print('/' * 79)
    print('')
    print("\U0001f44b Welcome to the number guessing game! \U0001f44b".title().center(75))
    if high_score != 0:
        print(f"High score: {str(high_score)}".center(75))
    print(' ')
    print("I'm thinking of a number between 1 and 10.".center(75))
    print("\U00002753 Try to guess it in as few attempts as possible. \U00002753".center(75))
    print(' ')
    print('/' * 79)
    print('/' * 79)
    print('')

    # Set per game variables
    number_to_guess = get_random_int()
    number_of_guesses = 0
    guess = input(
        f"Guess a number between {number_range_low} and {number_range_high}: ")

    while guess != number_to_guess:
        number_of_guesses += 1

        try:
            guess = int(guess)
        except ValueError:
            # Handle non-number guesses
            print("\U0001f61e That's not a valid number.")
        else:
            if guess < number_range_low:
                print(
                    f"Number not in range. Try higher between {number_range_low} and {number_range_high}! \U0001f446\U0001f446")
            elif guess > number_range_high:
                print(
                    f"Number not in range. Try lower between {number_range_low} and {number_range_high}! \U0001f447\U0001f447")
            elif guess > number_to_guess:
                print("It's lower!\U0001f447")
            elif guess < number_to_guess:
                print("It's higher! \U0001f446")

        if guess != number_to_guess:
            guess = input("Guess again: ")
        elif guess == number_to_guess:
            print('')
            print("You got it right!".center(75))
            print('')

            if high_score == 0 or number_of_guesses < high_score:
                high_score = number_of_guesses
                print(
                    f"\U0001f389 You set a new high score!: {number_of_guesses} \U0001f389".center(75))
            else:
                print(
                    f"It took you {number_of_guesses} tries to guess the number.".center(75))
                print(f"The high score is still: {high_score}.".center(75))

            print('')

    play_game = input("Do you want to play again? (Y/N): ")

print('')
print('Thanks for playing!')
print('')
