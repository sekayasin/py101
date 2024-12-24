# Dice Rolling Game
# Write a program that simulates rolling a pair of dice.
# Each time the program runs, it should randomly generate two numbers between a and 6 (inclusive), representing the result of each die.
# The program should then display the results and ask if the user would like to roll the dice again.
# Optional Enhancements
# - Modify the program so the user can specify how many dice they want to roll.
# - Add a feature that keeps track of how many times the user has rolled the dice during the session. This will require
# a counter that increments each time the dice are rolled.

# Solution
import random


def roll_dice(num_dice):
    if num_dice < 1:
        raise ValueError("Number of dice must be greater than 0")
    return [random.randint(1, 6) for _ in range(num_dice)]


roll_count = 0
waiting_for_input = True
while waiting_for_input:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y":
        num_dice = int(input("How many dice would you like to roll? "))
        if num_dice < 1:
            print("Invalid input. Please enter a number greater than 0")
            continue
        elif num_dice == 1:
            results = roll_dice(num_dice)[0]
        else:
            results = tuple(roll_dice(num_dice))
        roll_count += 1
        print(f"Results: {results}")
    elif choice == "n":
        print("Thanks for playing!")
        waiting_for_input = False
    else:
        print("Invalid input. Please enter 'y' or 'n'")
else:
    print("Game Over!")
print(f"Total rolls: {roll_count}")
