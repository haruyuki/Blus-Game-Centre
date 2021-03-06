# -*- coding: utf-8 -*-
# Blu's Game Centre v1.0
# Aiyurn © 2016

from random import randint
from time import sleep as s
from games import arithmetic, numguess, bluadventure
from definitions import sprint, progressbar, ask_name

# Introduction - Variables
game_choice = ""
menu_time = 0  # TODO Fix up some menutime issues
give_name = ""
asked_name = 0

# Start - Game Choice input options
game_arithmetic = ["1", "a", "arithmetic"]
game_numguess = ["2", "n", "number guess"]
game_cyoa = ["3", "c", "cyoa", "choose your own adventure"]

# --------------- CODE BEGINS HERE ---------------

print("Blu's Game Centre v1.0")
print("Aiyurn (C) 2016\n")
s(1)
print("-------------------------------- WARNING --------------------------------\n"
      "Tailstar told me to remind you beforehand to not spam the enter button!\n"
      "He says that it will not only ruin the experience, but also screw up\n"
      "the code as you are inputting 'enter' for the upcoming inputs!\n"
      "-------------------------------------------------------------------------\n"
      "\n"
      "Now with that out of the way, let's play!")
items = list(range(0, 110))
i = 0
l = len(items)

# Initial call to print 0% progress
progressbar(i, l, prefix='Loading:', suffix='Complete', barlength=50)
for item in items:
    # Do stuff...
    s(0.1)
    # Update Progress Bar
    i += 1
    progressbar(i, l, prefix='Loading:', suffix='Complete', barlength=50)
print()

while game_choice == "":
    # Introduction text
    if menu_time == 0:  # If this is the first time the user is accessing this menu
        sprint("Welcome to my Game Centre!\n", "default", "period")
        sprint("I'm Blu, ", "default", "comma")
        sprint("and I'll be joining you in the games you play in this program!\n", "default", "period")
        sprint("Here are the games you can choose from:\n", "default", "colon")
        sprint("1) Arithmetic (Multiplication)\n", "faster", "list")
        sprint("2) Number Guess\n", "faster", "list")
        sprint("3) Blu's Adventures [BETA]\n", "faster", "list")
        sprint("4) Tactical World [IN DEVELOPMENT]\n", "faster", "list")
        sprint("5) Word Jam [IN DEVELOPMENT]\n", "faster", "period")
        sprint("So, ", "default", "comma")
        sprint("what game do you want to play?\n", "default", "input")
    else:  # If the user has already accessed this menu i.e. coming back from a game
        print("And we're back at the menu again! What game do you want to play now?")
        print("Here are the games:\n"
              "1) Arithmetic (Multiplication)\n"
              "2) Number Guess\n"
              "3) Find-a-word [IN DEVELOPMENT]\n"
              "4) Blu's Adventures [BETA]\n"
              "5) Guess the country [IN DEVELOPMENT\n"
              "6) Letter Scramble [IN DEVELOPMENT")
    game_choice = input("> ")

    if asked_name == 0:  # A check to see whether the user has given his/her name.
        name = ask_name()
        asked_name = 1
    else:
        continue

    while True:
        value = randint(1, 5)  # Random number to determine which message to be displayed
        if game_choice in game_arithmetic:  # If the user selects the game Arithmetic
            if value == 1:
                # Let's check out your maths skills!
                sprint("Let's check out your maths skills!", "default", "mark")
            elif value == 2:
                # 6 x 5 is 11 right? No? Maybe I should just leave the maths to Tailstar...
                sprint("6 x 5 is 11 right?", "default", "mark")
                sprint("No? ", "default", "mark")
                sprint("Maybe I should just leave the maths to Tailstar...", "default", "period")
            elif value == 3:
                # Arithmetic? Sure let's go!
                sprint("Arithmetic? ", "default", "mark")
                sprint("Sure let's go!", "default", "mark")
            elif value == 4:
                # So you like maths I see... Let's see how good you are!
                sprint("So you like maths I see... ", "default", "period")
                sprint("Let's see how good you are!", "default", "mark")
            elif value == 5:
                # I, Blu, challenge you to a maths battle!
                sprint("I, ", "default", "comma")
                sprint("Blu, ", "default", "comma")
                sprint("challenge you to a maths battle!", "default", "mark")
            s(2)
            print("\n" * 2)
            arithmetic()
            game_choice = ""  # Reset gamechoice to enter back into the while loop
            menu_time = 1
            break
        elif game_choice in game_numguess:  # If the user selects the game Number Guess
            if value == 1:
                # Let's see if you can beat me, the legendary Blu!
                sprint("Let's see if you can beat me, ", "default", "comma")
                sprint("the legendary Blu!", "default", "mark")
            elif value == 2:
                # So you like number guessing, just like Tailstar!
                sprint("So you like number guessing, ", "default", "comma")
                sprint("just like Tailstar!", "default", "mark")
            elif value == 3:
                # Good choice! Let's begin!
                sprint("Good choice! ", "default", "mark")
                sprint("Let's begin!", "default", "mark")
            elif value == 4:
                # If you're planning to play easy mode, I'm going to guess that the number will be ***!
                number = str(randint(1, 1000))
                sprint("If you're planning to play easy mode, ", "default", "comma")
                sprint("I'm going to guess that the number will be" + number + "!", "default", "mark")
            elif value == 5:
                # I wonder if you'll beat me and Tailstar's high-scores... Let's play and see!
                sprint("I wonder if you'll beat me and Tailstar's high-scores... ", "default", "period")
                sprint("Let's play and see!", "default", "mark")
            s(2)
            print("\n"*2)
            numguess()
            game_choice = ""  # Reset gamechoice to enter back into the while loop
            menu_time = 1
            break

        elif game_choice in game_cyoa:  # If the user selects the game Blu's Adventure
            if value == 1:
                # I knew it! You are the adventurous type! COme on Tailstar is waiting for us!
                sprint("I knew it! ", "default", "mark")
                sprint("You are the adventurous type! ", "default", "mark")
                sprint("Come on Tailstar is waiting for us!", "default", "mark")
            elif value == 2:
                # You like adventures too? Come join me in my adventures with Tailstar!
                sprint("You like adventures too? ", "default", "mark")
                sprint("Come join me in my adventures with Tailstar!", "default", "mark")
            elif value == 3:
                # Everyone loves adventures! Especially when I'm in it! ...Right?
                sprint("Everyone loves adventures! ", "default", "mark")
                sprint("Especially when I'm in it! ", "default", "mark")
                sprint("...Right?", "slower", "mark")
            elif value == 4:
                # You're joining my adventure? Yay! We must hurry to the meeting point!
                sprint("You're joining my adventure? ", "default", "mark")
                sprint("Yay! ", "fast", "mark")
                sprint("We must hurry to the meeting point!", "default", "mark")
            elif value == 5:
                # Hopefully my adventure doesn't have that 'breaking the fourth wall' people have been talking about...
                sprint("Hopefully my adventure doesn't have that ", "default", "quote")
                sprint("'breaking the fourth wall' people have been talking about...", "default", "period")
            s(2)
            print("\n"*2)
            bluadventure()
            game_choice = ""
            menu_time = 1
            break

        elif game_choice == 'quit':  # If the user wants to quit
            if value == 1:
                # Why would you run this program if you weren't going to play anything...
                sprint("Why would you run this program if you weren't going to play anything...", "slow", "period")
            elif value == 2:
                # I tell you all these games you can play you tell me you want to leave?
                sprint("I tell you all these games you can play you tell me you want to leave?", "default", "mark")
            elif value == 3:
                # Tailstar created all this and you don't want to play anything?
                sprint("Tailstar created all this and you don't want to play anything?", "default", "mark")
            elif value == 4:
                # Didn't you like any of the games? Tell me a game you like and I'll get Tailstar to add it in!
                sprint("Didn't you like any of the games? ", "default", "mark")
                sprint("Tell me a game you like and I'll get Tailstar to add it in!", "default", "mark")
            elif value == 5:
                # If you want to quit... I guess I can't really stop you...
                sprint("If you want to quit... ", "default", "period")
                sprint("I guess I can't really stop you...", "slow", "period")
            quit()

        else:  # If the user selects a game that isn't in the list
            if value == 1:
                # Hey that's not an option!
                sprint("Hey that's not an option!\n", "default", "mark")
            elif value == 2:
                # I think you typed something wrong... There's no option for that.
                sprint("I think you typed something wrong... ", "default", "period")
                sprint("There's no option for that.\n", "default", "period")
            elif value == 3:
                # Are you purposely typing it wrong to get me to talk? If you are, it's not working!
                sprint("Are you purposely typing it wrong to get me to talk? ", "default", "mark")
                sprint("If you are, ", "default", "comma")
                sprint("it's not working!\n", "default", "mark")
            elif value == 4:
                # I don't think that option you typed is an option...
                sprint("I don't think that option you typed is an option...\n", "default", "period")
            elif value == 5:
                # Let's go and play something already! Don't choose a game that you can't play!
                sprint("Let's go and play something already! ", "default", "mark")
                sprint("Don't choose a game that you can't play!\n", "default", "mark")
            game_choice = input("> ")

    s(2)
