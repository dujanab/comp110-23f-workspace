"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730467698"

five_character_word: str = input("Enter a 5-character word: ")

if len(five_character_word) != 5:
    print("Word must contain 5 characters ")
    exit()

single_character: str = input("Enter a single character: ")

if len(single_character) == 1:
     print("Searching for " + single_character + " in " + five_character_word)
else:
     print("Character must be a single character. ")
     exit()

instances: int = 0

if single_character == five_character_word[0]:
     print(single_character + " found it at index 0")
     instances += 1

if single_character == five_character_word[1]:
     print(single_character + " found it at index 1")
     instances += 1

if single_character == five_character_word[2]:
     print(single_character + " found it at index 2")
     instances += 1

if single_character == five_character_word[3]:
     print(single_character + " found it at index 3")
     instances += 1

if single_character == five_character_word[4]:
     print(single_character + " found it at index 4")
     instances += 1

if instances == 0:
     print("No instances of " + single_character + " found in " + five_character_word)
elif instances == 1:
     print(str(instances) + " instance of " + single_character + " found in " + five_character_word)
else:
     print(str(instances) + " instances of " + single_character + " found in " + five_character_word)

