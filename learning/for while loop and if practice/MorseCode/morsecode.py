# morsecode.py
# Author: C.Maughan
# Date: 8/4/24

# Reflection: First time importing a personal module. I had to make sure the module was in the same
# directory as the file I was working on. But otherwise it is a surprisingly simple process.
# This program will convert a string of text into morse code

import morsecodeimport

def main():
    user_input = input("Enter a string of text to convert to morse code: ")
    for i in user_input:
        print(morsecodeimport.morse[i.upper()], end=" ")

if __name__ == "__main__":
    main()