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

    # Fill dict of words with value of frequency and prints name, wordcount, etc. to screen
    for rapper in rappertexts:
        words = fill_words(rapper)
        # Create rapper name from filefame (remove .txt and capitalize)
        rapper_name = rapper[:-4].capitalize()

        # TODO: Add comment
        rappers[rapper_name] = words

        # Create a dotted line for formating based on length of the rapper's name
        line = "." * (40 - len(rapper_name))

        print("%s%s\n\tWord Count: %s\n\tLargest Word: %s\n\tMost Used Word: %s" % \
              (rapper_name, line, len(rappers[rapper_name]), \
              max(rappers[rapper_name], key=len), max(rappers[rapper_name], \
              key=rappers[rapper_name].get)))

# Fills and returns a set of words for a given rapper file
def fill_words(rapper):
    words = []

    with open("lyrics/" + rapper, "r") as f:
        words = f.read().split()

    word_usage = {word: words.count(word) for word in set(words)}

    return word_usage

if __name__ == '__main__':
    main()
