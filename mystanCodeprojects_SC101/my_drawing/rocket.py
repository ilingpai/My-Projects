"""
File: rocket.py
Name:
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 5


def main():
    """
    draw a rocket.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):
        for j in range(SIZE-i):  # SIZE * space
            print(" ", end='')
        for j in range(i+1):
            print("/", end='')
        for j in range(i+1):
            print("\\", end='')
        print("")  # change line


def belt():
    for i in range(1):
        for j in range((2*SIZE+2)):
            if j == 0:  # j=0 must be +
                print("+", end="")
            elif j == (2*SIZE+1):  # last one must be +
                print("+", end="")
            else:  # others put =
                print("=", end="")
        print("")


def upper():
    for i in range(SIZE):
        for j in range(0, 1):
            print("|", end="")
        for j in range(SIZE-1-i):
            print(".", end="")
        for j in range(i+1):
            print("/\\", end="")
        for j in range(SIZE-1-i):
            print(".", end="")
        print("|", end="")
        print("")


def lower():
    for i in range(SIZE):
        for j in range(0, 1):
            print("|", end="")
        for j in range(i):
            print(".", end="")
        for j in range(SIZE-i):
            print("\\/", end="")
        for j in range(i):
            print(".", end="")
        print("|", end="")
        print("")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
