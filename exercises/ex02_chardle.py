"""chardle: off brand wordle"""

__author__ = "730698509"


def main() -> None:
    return contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """input a five letter word"""
    word = str(input("Enter a 5-character word: "))
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    else:
        return word


# you can't use the less/greater than operator or random because it's a str
# you have to use the len operator


def input_letter() -> str:
    """input a single character"""
    chr = str(input("Enter a single character: "))
    if len(chr) > 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        return chr


# put the exit function after the error because we still want the error displayed


# count has to start at 0 because before the search starts there are 0 instances
# in order to store the input_word i assigned it to the word variable
# I also assigned input_letter to letter
def contains_char(word: str, letter: str) -> None:
    count = 0
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    # instances based on count
    if count > 0:
        if count == 1:
            print(str(count) + " instance of " + letter + " found in " + word)
        else:
            print(str(count) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + str(letter) + " found in " + str(word))


if __name__ == "__main__":
    main()
