# morefunctionpractice.py
# Author: C.Maughan
# Date: 11/4/24

import datetime
import time


# Challenge 1: Takes user input for a currency conversion rate. User input of to or from this currency.
# User input of amount to convert. Function should return the converted amount.

def currency_conversion(rate, conversion, amount):
    if conversion == "to":
        return round(float(rate) * float(amount), 2)
    else:
        return round(float(amount) / float(rate), 2)


# Challenge 2: Maps a list of words into a list of integers representing the lengths of the corresponding words.

def word_length(words):
    return [len(word) for word in words]


# Challenge 3: Generates the bottles of beer song lyrics. Starting at the user input number of bottles.

def bottles_of_beer_song(bottles):

    while bottles > 0:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer."
              f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall.")
        bottles -= 1
        time.sleep(1)


# Main function to execute the challenges

def main():
    execute_challenge = input("Enter the number of the challenge you want to execute: ").lower().strip()

    if execute_challenge == "1":
        print(currency_conversion(input("Enter the conversion rate against the NZ dollar: "),
                                  input("Enter 'to' or 'from' this currency: ").lower().strip(),
                                  input("Enter the amount to convert: ")))
    elif execute_challenge == "2":
        print(word_length(input("Enter a list of words separated by a space: ").split()))

    elif execute_challenge == "3":
        bottles_of_beer_song(int(input("Enter the number of bottles of beer to start the song with: ")))


if __name__ == "__main__":
    main()
