"""Daily word game: You have 6 turns to guess the secret word"""

__author__ = "730698509"


# prompt user to guess a a 5 letter word using input
# if guess is less/more than 5 chars print "That wasn't 5 chars! Try Again:"
# use f strings and if using a variable: {variable}
def input_guess(secret_word_len: int) -> str:
    "input a five letter word"
    guess = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try Again: ")
    else:
        return guess


# check to see if each index of guess word matches char and return a true/false value
# only need one instance to return true
# no fixed length
def contains_char(secret_word: str, char_guess: str) -> bool:
    """this functions will sestch to see if the inputted char is in the secret word"""
    assert len(char_guess) == 1
    count = 0
    while count < len(secret_word):
        if char_guess == secret_word[count]:
            return True
        count = count + 1
    return False


# use contains_char to determine if yellow or white box is used
# 1st check if char of guess matches char of secret at same index and return green box
# 2nd check if char of guess word is present at all in secret using contains char
# if so return yellow box
# if requirements in 1st and 2nd check aren't met then return white box
def emojified(guess: str, secret: str) -> str:
    """use colored emojis to tell user how accurate their guess is"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emojis: str = ""
    count = 0
    while count < len(guess):
        if guess[count] == secret[count]:
            emojis = emojis + GREEN_BOX
        elif contains_char(secret_word=secret, char_guess=guess[count]):
            emojis = emojis + YELLOW_BOX
        else:
            emojis = emojis + WHITE_BOX
        count += 1
    return emojis


# i need to keep track of secret_word_len by assigning it the len of secret
# also keep track of guess, secret from emojified function
# prompt user for guess using input guess to make sure it's correct len
# after game loop print how many times it took them to win or prompt to try again
# keep track of number of turns
def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 0
    user_guess: str = ""
    while turn < 6 and user_guess != secret:
        print(f"=== Turn {turn + 1}/6 === ")
        user_guess = input_guess(len(secret))
        print(emojified(user_guess, secret))
        turn += 1
    if user_guess == secret:
        print(f"You won in {turn}/6 turns! ")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
