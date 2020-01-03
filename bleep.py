from cs50 import get_string
from sys import argv

words = set()


def main():

    if len(argv) != 2:
        print("Usage: python bleep.py dictionary")
        exit(1)

    load(argv[1])

    user_in = get_string("What message would you like to censor? \n")
    tokens = user_in.split()

    for i in tokens:
        if check(i):
            for j in i:
                print("*", end="")
        else:
            print(i, end="")
        print(" ", end="")

    print()

    return True


def load(banned):
    file = open(banned, "r")
    for line in file:
        words.add(line.rstrip("\n"))
    file.close()
    return True


def check(word):
    return word.lower() in words


if __name__ == "__main__":
    main()