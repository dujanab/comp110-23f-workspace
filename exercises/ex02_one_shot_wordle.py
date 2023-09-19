"""EX02 - One-shot Wordle"""
__author__ = "730467698"

#defining secret word and user input
secret_word: str = "python"

#hat happens if length of user input < length of secret word
user_input: str = input(f"What is your {len(secret_word)}-letter guess? ")
while len(user_input) != len(secret_word):
    user_input = input(f"That was not {len(secret_word)} letters! Try again: ")

#defining emoji boxes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

#keeping track of user input index and establishing resulting emoji to empty string
character_idx: int = 0
resulting_emoji: str = ""

#rules for concatenating color box emojis based on current index of user input and secret word
while character_idx < len(secret_word):
    if user_input[character_idx] == secret_word[character_idx]:
        resulting_emoji += GREEN_BOX
    else:
        #location where current index of user word does not match same index of secret word
        existing_guessed_character: bool = False
        alternate_idx: int = 0
        while (not existing_guessed_character) and (alternate_idx < len(secret_word)):
            if secret_word[alternate_idx] == user_input[character_idx]:
                existing_guessed_character = True
            else:
                alternate_idx += 1
        if existing_guessed_character:
            resulting_emoji += YELLOW_BOX
        else:
            resulting_emoji += WHITE_BOX
    character_idx += 1 

#what happens if user input = secret word letters, but does not = secret word
if user_input != secret_word:
    print(f"{resulting_emoji}")
    print(f"Not quite. Play again soon! ")

#what happens if user input = secret word
if user_input == secret_word:
    print(f"{resulting_emoji}")
    print(f"Woo! You got it!")