#!/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Dec 14, 2021
# This program gets the user to guess a number
# between 0 and 9 and tells them if it is correct.
import random


def main():
    # set the correct number
    correct = random.randint(0, 9)

    # get user input
    user_number_string = input("Enter your number: ")
    print("")

    # error checking
    try:
        # convert user number to int
        user_number = int(user_number_string)

        # check number size
        if user_number >= 10:
            print("Number must be between 0 and 9.")

        elif user_number <= -1:
            print("Number must be between 0 and 9.")

        # check if user number is correct
        elif user_number == correct:
            print("Correct!")

        else:
            print("Wrong, the number was {}.". format(correct))

    except Exception:
        print("Your input, {}, was not a number". format(user_number_string))

    finally:
        print("Thank you for playing")


if __name__ == "__main__":
    main()
