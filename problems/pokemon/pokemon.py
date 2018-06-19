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

# TODO: Create a list of type Pokémon names (as strings) and store in pokeNames
pokeNames = []


def main():
    # List of Pokémon objects
    pokeList = []
    populate(pokeList)

    while(true):
        myPokemon = selectPokemon(pokeList)
        myMove = selectMove(myPokemon)
        print("%s perfomed %s, dealing %i damage!", myPokemon.name, move.name, move.damage)
        print

# Populate each Pokémon with hp, type, and move names and add to pokeList
def populate(pokemon):
    # TODO

def printPokemon(pokemon):
    print("The Pokémon you have access to are:")
    for poke in pokemon
        print(poke.name)
    print("-----------------------------------")

# Ask user for Pokémon and return approprate Pokemon object
def selectMove(poke):
    print("The Moves %s can preform to are:", poke.name)

    for move in poke.moves:
        print("%s: %s damage", move.name, move.damage)
    print("--------------------------------")

    # TODO: Ask user for a Pokémon and return approprate Pokemon object when actual
    # Pokémon has been found
    # Hint: look at selectPokemon() for inspiration

# Ask user for Pokémon and return approprate Pokemon object
def selectPokemon(pokemon):
    print("The Pokémon you have access to are:")
    for poke in pokemon
        print(poke.name)
    print("-----------------------------------")

    while (true):
        iChooseYou = get_string("Which Pokémon would you like to select? ")
        for poke in pokemon:
            if iChooseYou == poke.name:
                return poke
        print("Invalid Pokémon!")

if __name__ == '__main__':
    main()
