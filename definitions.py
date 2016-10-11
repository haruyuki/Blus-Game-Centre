import sys
from time import sleep
from random import randint

# http://stackoverflow.com/questions/22886353/printing-colors-in-python-terminal
# http://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
# http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

def color(type):
    if type == "bold_white":
        return "\033[1;37m"
    elif type == "bold_yellow":
        return "\033[1;33m"
    elif type == "bold_green":
        return "\033[1;32m"
    elif type == "bold_blue":
        return "\033[1;34m"
    elif type == "bold_cyan":
        return "\033[1;36m"
    elif type == "bold_red":
        return "\033[1;31m"
    elif type == "bold_magenta":
        return "\033[1;35m"
    elif type == "bold_black":
        return "\033[1;30m"
    elif type == "white":
        return "\033[0;37m"
    elif type == "yellow":
        return "\033[0;33m"
    elif type == "green":
        return "\033[0;32m"
    elif type == "blue":
        return "\033[0;34m"
    elif type == "cyan":
        return "\033[0;36m"
    elif type == "red":
        return "\033[0;31m"
    elif type == "magenta":
        return "\033[0;35m"
    elif type == "black":
        return "\033[0;30m"
    elif type == "off":
        return "\033[0;0m"
# print(color("bold_white") + "I'm white! " + color("bold_yellow") + "I'm yellow!")


def sprint(text, speed, delay):  # Print out text with a custom speed
    for c in text:
        print(c, end=""),
        sys.stdout.flush()
        if speed == "normal":  # Normal printing speed
            sleep(0.035)
        if speed == "slack":  # Slow printing speed
            sleep(0.05)
        if speed == "slower":  # Slower printing speed
            sleep(0.06)
        if speed == "super":  # Fastest printing speed
            sleep(0.02)
        if speed == "faster":  # Faster printing speed
            sleep(0.03)
    if delay == "comma":  # If the last punctuation is a comma (,)
        sleep(0.45)
    elif delay == "period":  # If the last punctuation is a period (.)
        sleep(1)
    elif delay == "quote":  # If the last punctuation is quotes ("")
        sleep(0.1)
    elif delay == "colon":  # If the last punctuation is a colon (:)
        sleep(0.3)
    elif delay == "list":  # If the last punctuation is a list of something
        sleep(0.05)
    elif delay == "mark":  # If the last punctuation is a punctuation mark (! ?)
        sleep(0.5)
    elif delay == "input":  # If the next code asks for an input
        sleep(0.05)

def progressbar(iteration, total, prefix='', suffix='', decimals=1, barlength=100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    formatstr = "{0:." + str(decimals) + "f}"
    percents = formatstr.format(100 * (iteration / float(total)))
    filledlength = int(round(barlength * iteration / float(total)))
    bar = '█' * filledlength + '-' * (barlength - filledlength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

'''
#
# Sample Usage
#

from time import sleep

# make a list
items = list(range(0, 100))
i = 0
l = len(items)

# Initial call to print 0% progress
progressbar(i, l, prefix='Progress:', suffix='Complete', barLength=50)
for item in items:
    # Do stuff...
    sleep(0.1)
    # Update Progress Bar
    i += 1
    progressBar(i, l, prefix='Progress:', suffix='Complete', barLength=50)
'''


def ask_name():
    # Oh that reminds me! I still don't know your name yet!
    # Do you want to tell me your name? You don't have to, but it would be nice if you did!
    sprint("Oh that reminds me! ", "faster", "mark")
    sprint("I still don't know your name yet! ", "normal", "mark")
    sprint("Do you want to tell me your name? ", "normal", "mark")
    sprint("You don't have to, ", "slack", "comma")
    sprint("but it would be nice if you did!\n", "faster", "period")
    print("Do you want to give your name? (Yes / No)")
    sleep(0.7)
    give_name = input("> ")
    give_name = give_name.lower()
    while True:
        value = randint(1, 5)
        if give_name == "yes":
            if value == 1:
                # Yay! So what is your name?
                sprint("Yay! ", "normal", "mark")
                sprint("So what is your name?\n", "normal", "mark")
            elif value == 2:
                # You're name doesn't happen to be Tailstar, is it? If it is, then I already know you!
                sprint("You're name doesn't happen to be Tailstar, ", "normal", "comma")
                sprint("is it? ", "normal", "mark")
                sprint("If it is ", "normal", 0)
                sprint("then I already know you!\n", "faster", "mark")
            elif value == 3:
                # Let's see what cool name you have!
                sprint("Let's see what cool name you have!\n", "normal", "mark")
            elif value == 4:
                # Tailstar told me to look out for people with names 'Riley' or 'Michael'.
                # That doesn't happen to be you is it?
                sprint("Tailstar told me to look out for people with names ", "normal", "quote")
                sprint("'Riley' or ", "normal", "quote")
                sprint("'Michael'. ", "normal", "period")
                sprint("That doesn't happen to be you is it?\n", "normal", "mark")
                print("dasdas", "asdasdas", )
            elif value == 5:
                # I was going to guess your name, but that would be too hard wouldn't it?
                sprint("I was about to guess your name, ", "normal", "comma")
                sprint("but that would be too hard wouldn't it?\n", "normal", "mark")
            value = randint(1, 5)
            print("Please enter your name.")
            name = input("> ")
            if name == "Michael":
                if value == 1:
                    print()
                elif value == 2:
                    print()
            print()
            break
        elif give_name == "no":
            if value == 1:
                # Oh... That's fine, let's continue to the game then...
                sprint("Oh... ", "slack", "period")
                sprint("That's fine, ", "slack", "comma")
                sprint("let's continue to the game then...\n", "slack", "period")
            elif value == 2:
                # I see... I did say you don't have to give it, let's go on to your game.
                sprint("I see... ", "slack", "period")
                sprint("I did say you don't have to give it, ", "slack", "comma")
                sprint("let's go on to your game.\n", "slack", "period")
            elif value == 3:
                # It would've been nice to call you by a name...
                sprint("It would've been nice to call you by a name...\n", "slack", "period")
            elif value == 4:
                # I guess I'm going to be still referencing you as... Well, you...
                sprint("I guess I'm going to be still referencing you as... ", "slack", "period")
                sprint("Well, ", "slack", "comma")
                sprint("you...\n", "slack", "period")
            elif value == 5:
                # So, no name? Ok then, off to the game we go...
                sprint("So, ", "slack", "comma")
                sprint("no name? ", "slack", "mark")
                sprint("Ok then, ", "slack", "comma")
                sprint("off to the game we go...\n", "slack", "period")
            sleep(1.5)
            break
        else:
            if value == 1:
                # Wait... So are you giving me your name?
                sprint("Wait... ", "normal", "period")
                sprint("So are you giving me your name?\n", "normal", "mark")
            elif value == 2:
                # I don't know what you just typed, but for all I know it isn't one of the options!
                sprint("I don't know what you just typed, ", "normal", "comma")
                sprint("but for all I know it isn't one of the options!\n", "normal", "mark")
            elif value == 3:
                # A simple question and a simple answer... Well, maybe not the answer, but typing the answer is simple!
                sprint("A simple question and simple answer... ", "normal", "period")
                sprint("Well, ", "normal", "comma")
                sprint("maybe not the answer, ", "normal", "comma")
                sprint("but typing the answer is simple!\n", "normal", "mark")
            elif value == 4:
                # Names... Such a strange thing... But back to the point, you didn't type one of the options!
                sprint("Names... ", "slack", "period")
                sprint("Such a strange thing... ", "slack", "period")
                sprint("But back to the point, ", "normal", "comma")
                sprint("you didn't type one of the options!\n", "normal", "mark")
            elif value == 5:
                # I thought I asked a simple yes or no question... I guess it wasn't so simple?
                sprint("I thought I asked a simple yes or no question... ", "normal", "period")
                sprint("I guess it wasn't so simple?", "normal", "mark")
            give_name = input("> ")
