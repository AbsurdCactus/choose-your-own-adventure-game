from ascii_art import intro_art

def gooby():
    print("hello world")
def get_input():
    return input()


def start():

    print(intro_art)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    first_step()


def first_step():

    print("Type \"left\" to go left, \"right\" to go right: ")
    first_choice = get_input()

    if first_choice == "L":
        print("you go left")
        second_step()

    else:
        print("You fall into a hole. Game over")


def second_step():

    print("Choose S for swim, W for wait: ")

    second_choice = get_input()

    if second_choice == "W":
        print("You wait")
        third_step()

    else:
        print("Attacked by trout. Game over")


def third_step():

    print("Choose R for Red, B for blue, Y for yellow: ")
    third_choice = get_input()

    if third_choice == "Y":
        print("You Win!")

    elif third_choice == "R":
        print("Burned by fire. Game Over.")

    elif third_choice == "B":
        print("Eaten by beasts. Game over")

    else:
        print("Game Over")


start()
