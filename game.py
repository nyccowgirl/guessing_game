"""A number-guessing game."""

# greet player
# get player name
# choose random number between 1 and 100
# repeat forever:
#     get guess
#     if guess is incorrect:
#         give hint
#         increase number of guesses
#     else:
#         congratulate player
import random

def greet_player(player_name):
    """welcome the player by name--which comes from user input"""
    print "Hello {}! Welcome to the number guessing game!\n\n".format(get_player_name())

def get_player_name():
    while True:
        player_name = raw_input("What is your name? >")
        if player_name.isdigit():
            print "That is not a real name...come on bro...get it together"
        else:
            return player_name.title()

def validate_number():
    """validate user number to ensure it is integer, returns integer"""
    while True:
        user_input = raw_input("What number do you guess? >")

        if not user_input.isdigit():
            print "That is not a valid input...try again"
        else:
            return int(user_input)

def guessing_game():
    """# repeat forever:
    get guess
    if guess is incorrect:
        give hint
        increase number of guesses
    else:
        congratulate player """

    greet_player(get_player_name())

    secret_number = random.randint(1, 100)
    high_limit = 100
    low_limit = 1
    guess = None

    while True:
        print "It's lower than {} and higher than {}.\nGood luck!".format(high_limit, low_limit)
        guess = validate_number()
        if guess > secret_number:
            print "Guess is too high"
            high_limit = guess
        elif guess < secret_number:
            print "Guess is too low"
            low_limit = guess
        else:
            print "Congrats! {} is the secret number!".format(secret_number)
            break


guessing_game()

# for when we start troubleshooting for assholes like us who can't follow directions...
# if guess > high_limit or guess < low_limit:
        #     print "That is not a valid guess."