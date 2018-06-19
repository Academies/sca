from cs50 import get_string
from helpers import *

def main():
    greet()
    # List of Pokemon objects
    pokeList = []
    populate(pokeList)

    while(True):
        myPokemon = selectPokemon(pokeList)
        lineBreak()

        myMove = selectMove(myPokemon)
        lineBreak()

        print("{} perfomed {}, dealing {} damage!".format(myPokemon.name, myMove.name, myMove.damage))
        lineBreak()

        while (True):
            play = get_string("Keep playing? (Y/N) ")
            if play == "Y":
                break
            elif play == "N":
                print("Thanks for playing!")
                return

if __name__ == '__main__':
    main()
