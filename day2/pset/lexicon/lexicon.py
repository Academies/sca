#!/usr/bin/python3

import os

def main():
    rappertexts = []

    # Directory where lyrics are stored
    directory = os.fsencode("lyrics/")

    # Fill list of rappers with txt filenames
    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        if filename.endswith(".txt"):
            rappertexts.append(filename)
            continue
        else:
            continue
    # Create a dict that has a rapper name and then set of words
    rappers = dict()

    # Fill dict and prints name and wordcount to screen
    for rapper in rappertexts:
        word_set = fill_words(rapper)
        rapper_name = rapper[:-4]
        rappers[rapper_name] = word_set
        line = "." * (40 - len(rapper_name))
        print("%s%s\n\tword count: %s\n\tlargest word:%s" % (rapper_name.capitalize(), \
              line, len(rappers[rapper_name]), max(rappers[rapper_name], key=len)))

# Fills and returns a set of words for a given rapper file
def fill_words(rapper):
    words = []

    with open("lyrics/" + rapper, "r") as f:
        words = f.read().split()

    return set(words)

if __name__ == '__main__':
    main()
