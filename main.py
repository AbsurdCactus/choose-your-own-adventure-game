from ascii_art import intro_art

print(intro_art)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
the_string = "hello world"


def starting_up():
    # print(the_string)
    return the_string


def start_game():

    first_choice = input("Choose L for left, R for right: ")

    if first_choice == "L":

        print("you go left")

    else:

        print("You fall into a hole. Game over")
        exit

    second_choice = input("Choose S for Swim, W for wait: ")

    if second_choice == "W":

        print("You wait")

    else:

        print("Attacked by trout. Game over")
        exit

    third_choice = input("Choose R for Red, B for blue, Y for yellow: ")

    if third_choice == "Y":

        print("You Win!")
        exit

    elif third_choice == "R":

        print("Burned by fire. Game Over.")
        exit

    elif third_choice == "B":
        print("Eaten by beasts. Game over")
        exit

    else:

        print("Game Over")
        exit


start_game()
