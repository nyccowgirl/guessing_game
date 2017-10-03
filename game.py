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
    print "Hello {}! Welcome to the number guessing game!".format(get_player_name())


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
    secret_number = random.randint(1, 100)
    high_limit = 100
    low_limit = 1
    while True:
        guess = 