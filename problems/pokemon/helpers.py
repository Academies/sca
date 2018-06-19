from cs50 import get_int, get_string
from time import sleep

class Move:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Pokemon:
    def __init__(self, name, pokeType, hp, moves):
        self.name = name
        self.type = pokeType
        self.hp = hp
        self.moves = moves

    def addMove(self, move):
        self.moves.append(move)

def greet():
    print("Welcome to")
    print("                                  ,'\\\n"
          "    _.----.        ____         ,'  _\   ___    ___     ____\n"
          "_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.\n"
          "\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |\n"
          " \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |\n"
          "   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |\n"
          "    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |\n"
          "     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |\n"
          "      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |\n"
          "       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |\n"
          "        \_.-'       |__|    `-._ |              '-.|     '-.| |   |\n"
          "                                `'                            '-._|\n"
          )
    sleep(1)

def lineBreak():
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# Populate each Pokemon with hp, type, and move names and add to pokeList
def populate(pokemon):
    while(True):
        pokeName = ""

        while (True):
            pokeName = get_string("Enter the name of a Pokemon (enter 'done' to quit adding Pokemon): ")
            lineBreak()

            if pokemon or pokeName != "done":
                break
            else:
                print("You must enter at least one Pokemon!")

        if pokeName == "done":
            break

        pokeType = get_string("Enter the type of {}: ".format(pokeName))
        hp = get_int("Enter the hp of {}: ".format(pokeName))

        lineBreak()

        moves = []
        print("Please enter 4 moves for {}.".format(pokeName))

        for i in range(4):
            moveName = get_string("Enter the name of move {}: ".format(i + 1))
            damage = get_int("Enter the damage of move {}: ".format(i + 1))
            move = Move(moveName, damage)
            moves.append(move)

        poke = Pokemon(pokeName, pokeType, hp, moves)
        pokemon.append(poke)

        print("Pokemon added!")
        lineBreak()

def printPokemon(pokemon):
    print("The Pokemon you have access to are:")
    for poke in pokemon:
        print(poke.name)
        lineBreak()

# Ask user for Pokemon and return approprate Pokemon object
def selectMove(poke):
    print("The Moves {} can preform to are:".format(poke.name))

    for move in poke.moves:
        print("{}: {} damage".format(move.name, move.damage))
    lineBreak()

    # TODO: Ask user for a Pokemon and return approprate Pokemon object when actual
    # Pokemon has been found
    # Hint: look at selectPokemon() for inspiration

    while (True):
        iChooseYou = get_string("Which Move would you like to select? ")
        for move in poke.moves:
            if iChooseYou == move.name:
                return move
        print("Invalid move!")

# Ask user for Pokemon and return approprate Pokemon object
def selectPokemon(pokemon):
    print("The Pokemon you have access to are:")
    for poke in pokemon:
        print(poke.name)
    lineBreak()

    while (True):
        iChooseYou = get_string("Which Pokemon would you like to select? ")
        for poke in pokemon:
            if iChooseYou == poke.name:
                return poke
        print("Invalid Pokemon!")
