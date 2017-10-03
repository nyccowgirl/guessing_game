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
    print "Hello {}! Welcome to the number guessing game!\n\n".format(player_name)

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

        try:
            user_input = int(user_input)
        except ValueError:
            print "That is not a number...You know better\nI hope.\n"
        except IndexError:  # never gonna happen, but for educational purposes, know it exists
            print "This will never print"
        except:  # never gonna happen, but for educational purposes, know it exists
            print "Any other type of exception will trigger this"
        else:
            break

    return user_input

def guessing_game():
    """# repeat forever:
    get guess
    if guess is incorrect:
        give hint
        increase number of guesses
    else:
        congratulate player """

    player_name = get_player_name()
    greet_player(player_name)

    secret_number = random.randint(1, 100)
    high_limit = 100
    low_limit = 1
    num_guesses = 0

    while True:
        print "It's lower than {} and higher than {}.\nGood luck!\n".format(high_limit, low_limit)
        num_guesses += 1
        guess = validate_number()
        if guess > high_limit or guess < low_limit:
            print "That guess is outside the parameters...\ndipshit\n"
        elif guess > secret_number:
            print "Guess is too high\n"
            high_limit = guess
        elif guess < secret_number:
            print "Guess is too low\n"
            low_limit = guess
        else:
            print "Congrats! {} is the secret number!\nIt took you {} guesses".format(secret_number, num_guesses)
            if num_guesses <= 4:
                print "Wow, that's impressive!"
            else:
                print "What a dipshit!"
            break

guessing_game()

