"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SECRET = 7


def main():
    """
    Get the original content of the encrypted text and find the encrypted string of letters.
    """
    print("Secret Number: " + str(SECRET))
    decipher()


def decipher():
    new = str(input("what's the ciphered string? ")).upper()  # change to upper so they can find it in ALPHABET!
    new_alphabet = ALPHABET[26-SECRET:] + ALPHABET[:26-SECRET]  # WXYZABC...
    ans = ""
    for ch in new:
        i = new_alphabet.find(ch)  # use (ch) so we can find every single letter in ALPHABET
        if i != -1:
            ans += ALPHABET[i]
        else:
            ans += ch
    print("The deciphered string is: " + ans, end="")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
