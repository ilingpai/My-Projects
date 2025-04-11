"""
File: hailstone.py
Name:Sandy
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program compute Hailstone sequences and count how many steps it took.
    """
    print("This program compute Hailstone sequences.")
    n = int(input('Enter a number: '))
    h = 0  # count steps
    while n != 1:
        if n % 2 == 0:
            print(str(n) + " is even, so I take half: " + str(n//2))
            n = n // 2
            h += 1
            if n == 1:
                break
        if n % 2 == 1:
            print(str(n) + " is odd, so I make 3n+1: " + str(3*n+1))
            n = 3*n+1
            h += 1
            if n == 1:
                break
    print("It took " + str(h) + " steps to reach 1." )


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
