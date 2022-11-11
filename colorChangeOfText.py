#command code tell the computer to change the  color of text that follows  to a different color
print("\033[\textCOLORm")
#colores to choose:

print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person")

text = "The quick brown fox jumps over the lazy dog."
print('\033[1;32m'+text+'\033[1;m')


# Terminal color definitions


BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'
DEFAULT = "\033[0m"
intro = """Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!\n"""
name = input("What is your name? ")
enemy = input("What is your worst enemy\'s name?")
superpower = input("What is your superpower?")
place= input("Where do you live?")
food=  input("What is your favorite food?")

print(intro)

#adding color


print(f"Hello {name}!\n\n Your ability to {superpower} will make sure you never have {YELLOW} to look at {enemy} again {DEFAULT}.\n Go eat {food} as you walk down the streets of {BLUE, place, DEFAULT} and use {RED, superpower, DEFAULT} for {GREEN}good {DEFAULT} and not {RED}evil!{DEFAULT}")