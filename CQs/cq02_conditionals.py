"""a fun number guessing game!"""

__author__ = "730698509"


def guess_a_number() -> None:
    secret: int = 7
    x = int(input("Guess a number: "))
    print("Your guess was " + str(x))
    if x == secret:
        print("You got it!")
    else:
        if x < secret:
            print("Your guess was too low! The secret number is " + str(secret))
        else:
            print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
