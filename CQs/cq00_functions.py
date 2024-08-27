__author__ = "730698509"


"""Practice writing and calling a function"""


def mimic(message: str) -> str:
    """take input and repeat it back"""
    return message


if __name__ == "__main__":
    print(mimic(message=input("What is your message?")))
