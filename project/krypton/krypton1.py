#!/usr/bin/env python3

# It's not elegant but it worked :')

def splitString(s):
    # Split up into words
    return s.split(' ')

def rotWord(s, n):
    # Splits up the string, rotates the letters, then rejoins the string
    characters = list(s)
    new_characters = []
    for character in characters:
        new_characters.append(rotLetter(character, n))
    return "".join(new_characters)

def rotLetter(c, n):
    characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    index = 0
    while (characters[index] != c):
        index += 1
        index = index % 26
    index += n
    index = index % 26

    return characters[index]

def main():
    for word in splitString("YRIRY GJB CNFFJBEQ EBGGRA"):
        print(word + ":")
        for i in range(0, 26):
            print(f"    {rotWord(word, i)}")
main()

#solution: ROTTEN
