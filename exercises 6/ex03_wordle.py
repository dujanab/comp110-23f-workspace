"""EX03 - Structured Wordle."""
__author__ = "730467698"

def contains_char(searched_thru_word: str, searched_for_character: chr) -> bool:
    """Returns found character (True or False) if character can be found at any index of word."""
    assert len(searched_for_character) == 1

    # defining found character as False and establish character index
    found_character: bool = False
    character_idx: int = 0

    # what happens if we do find the found character/when it becomes True
    while (not found_character) and (character_idx < len(searched_thru_word)):
        if searched_for_character == searched_thru_word[character_idx]:
            found_character = True
        else:
            character_idx += 1 
    return found_character

def emojified(guessed_word: str, secret_word: str) -> str:
    """Returns resulting emoji based on if 
    1) guessed word char idx is equal to secret word char idx (green)
    2) guessed word char idx is equal to secret word char idx elsewhere (yellow)
    3) guessed word char idx is never equal to secret word char idx (white)."""
    assert len(guessed_word) == len(secret_word)

    # defining emoji boxes
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    # keeping track of user input index and establishing resulting emoji to empty string
    character_idx: int = 0
    resulting_emoji: str = ""

    # rules for concatenating color box emojis based on current index of guessed word and secret word 
    while character_idx < len(secret_word):
        if guessed_word[character_idx] == secret_word[character_idx]:
            resulting_emoji += GREEN_BOX
        else: 
            found_character = contains_char(secret_word, guessed_word[character_idx])
            if found_character == True:
                resulting_emoji += YELLOW_BOX
            else:
                resulting_emoji += WHITE_BOX
        character_idx += 1
    return resulting_emoji

def input_guess(expected_length: int) -> int:
    """Returns user input if user input len is equal to expected len."""

    # what happens if length of user input < length of secret word
    user_input: str = input(f"Enter a {expected_length} character word: ")
    while len(user_input) != expected_length:
        user_input = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_input

def main() -> None:
    """The entrypoint of the program and main game loop."""

    # location of secret word
    secret_word: str = "codes"

    # defining max turns and number of turns that the user has
    max_turns: int = 6
    number_of_turns: int = 1

    # what happens based on 1) how many turns user has left and
    # 2) if they guess the secret word before running out of turns
    while (number_of_turns <= (max_turns)):
        print(f'=== Turn {number_of_turns}/{max_turns} ===')
        guessed_word: str = input_guess(len(secret_word))
        resulting_emoji: str = emojified(guessed_word, secret_word)
        print(resulting_emoji)
        if guessed_word == secret_word:
            print(f'You won in {number_of_turns}/{max_turns} turns! ')
            exit()
        else:
            number_of_turns += 1
    print(f'X/{max_turns} – Sorry, try again tomorrow! ')

# allows us to run Wordle game as a module
if __name__ == "__main__":
    main()