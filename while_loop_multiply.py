#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program adds up positive integers
#    with numbers inputted from the user

def main():
    # this function adds up positive numbers

    loop_counter = 1

    # input
    positive_string = input("Enter an positive integer: ")

    # process

    # output
    try:
        positive_integer = int(positive_string)
        if positive_integer < 0:
            print("You did not enter a positive integer")
        elif positive_integer == 0:
            print()
        else:
            for i in range(1, positive_integer + 1):
                loop_counter = loop_counter * i
            # https://www.javatpoint.com/python-sum-natural-numbers
        while loop_counter <= positive_integer:
            i *= loop_counter
            loop_counter += 1
        print("{}! = {}".format(positive_integer, loop_counter))
    except Exception:
        print("{} is not an number".format(positive_string))
    finally:
        print("")


if __name__ == "__main__":
    main()
