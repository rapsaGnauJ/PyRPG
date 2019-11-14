#!/usr/bin/python3
import os

from keia import Keia
from creature import Creature
from monster import Monster

clear = lambda: os.system('clear') #on Linux System

# Initializations.
player = Keia(300, 25, 20, "Keia")
enemy = Monster(400, 20, 20, "Ugly monster")

turn_count = 1
enemy_last_action = "\n\n"

def game_end(msg):
    print_game()
    print("\n" + msg)
    print("Game over. Thanks for playing!")
    exit()

def print_game():
    
    clear() # Clear the console.
    
    # Print turn counter.
    print("---------- Turn " + str(turn_count) + " ----------")

    # Print player stats.
    player.print_stats_min()

    print("\n")
    
    # Print enemy stats.
    enemy.print_stats_min()

    # Print enemy last action.
    print(enemy_last_action)
    
    # Player turn.
    print("\tIts your turn! \n")
    print("\t1.- Attack.")
    print("\t2.- Special Attak.")
    print("\t3.- Exit the game.")


# Main game loop.
while (1) :

    print_game()
    
    action = input()

    if action == "1":
        # Attack the enemy.
        player.attack(enemy)

        # Check for death.
        if enemy.is_dead():

            #The player has won.
            game_end("You won!")
            
    elif action == "2":
        # Do a especial attack.
        player.special_attack(enemy)

        # Check for death.
        if enemy.is_dead():

            #The player has won.
            game_end("You won!")

    elif action == "3":
        game_end("You just surrendered. Too bad! Waluigi time!")

    # Enemy's turn.
    enemy.attack(player)
    enemy_last_action = "\n\tThe " + enemy.get_name() + " attacked!\n"
    
    # Check for death.
    if player.is_dead():
        # The player has lost.
        game_end("You lost. Try again.")


    turn_count += 1
