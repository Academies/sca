import os

rappers = []

directory = os.fsencode("lyrics/")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"):
        rappers.append(filename[:-4])
        continue
    else:
        continue

for rapper in rappers:
    words = []
    with open("lyrics/" + rapper + ".txt", "r") as f:
        words = f.read().split()

    word_set = set(words)

    print("%s\n  words: %s\n  largest word:%s" % (rapper.capitalize(), len(word_set), max(word_set, key=len)))
