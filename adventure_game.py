import time
import random

weapons = ["Staff", "Sword", "Spear", "Shield"]
items = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def playagain():
    global items
    items = []

    play_again = input("Would you like to play again? (y/n)")
    if play_again == "y":
        print_pause("The Game is Restarting!!!!!\n")
        field(items)
    elif play_again == "n":
        print_pause("Till next time!!! BYE....\n")
        return
    else:
        playagain()


def field(items):
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere"
                " around here, and has been terrifying the nearby village.")
    if len(items) == 0:
        print_pause("In front of you is a house.")
        print_pause("To your right is a dark cave.")
        print_pause("In your hand you hold your trusty"
                    " (but not very effective) dagger.")
    else:
        print_pause("In front of you is a house.")
        print_pause("To your right is a dark cave.")

    choice(items)


def choice(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    answer = input("(Please enter 1 or 2.)")
    print_pause("\n")
    if answer == '1':
        door_knock(items)
    elif answer == '2':
        enter_cave(items)
    else:
        print_pause("Wrong!\n"
                    "Try again")
        choice(items)


def door_knock(items):

    print_pause("You approach the door of the house.")
    print_pause("You are about to knock"
                " when the door opens and out steps a gorgon.")
    print_pause("Eep! This is the gorgon's house!")
    print_pause("The gorgon attacks you!\n")

    if len(items) == 0:
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger.")

    attack_or_escape = input("Would you like to (1) fight or (2) run away?\n")
    if attack_or_escape == "1":
        attack(items)
    if attack_or_escape == "2":
        escape()
    else:
        playagain()


def enter_cave(items):
    if len(items) == 0:
        items.append(random.choice(weapons))
        weapon = items[0]
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause(f"Your eye catches a glint of {weapon} behind a rock.")
        print_pause(f"You have found the magical {weapon} of Ogoroth!")
        print_pause("You discard your silly old dagger"
                    f" and take the {weapon} with you.")
        print_pause("You walk back out to the field.\n")
    else:
        print_pause(f"You have been here before and you picked a {weapon}\n"
                    "You are ready to fight anything and anyone")
    field(items)


def attack(items):
    if len(items) == 1:
        print_pause(f"As the troll moves to attack,"
                    " you unsheath your new {items[0]}.")
        print_pause(f"The {items[0]} shines brightly in your hand"
                    " as you brace yourself for the attack.")
        print_pause(f"But the troll takes one look"
                    " at your shiny new {items[0]} and runs away!")
        print_pause("You have rid the town of the troll."
                    " You are victorious!\n")
        playagain()
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the gorgon.")
        print_pause("You have been defeated!\n")
        playagain()


def escape():
    print_pause("You quickly returned back to the field\n"
                "And the dragon went back inside\n")
    field(items)


field(items)
