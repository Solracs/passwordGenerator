#!/bin/python3
# Made by: @Solracs

import sys
import secrets
import argparse

# list of all printable chars
printable = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

password = ""


#setting args parser up
parser = argparse.ArgumentParser()

parser.add_argument('-l', type = int, required = True, help = "passwod length")

parser.parse_args()

args = parser.parse_args()

if args.l:

    try:
        length = args.l

        for i in range(length):
            password += secrets.choice(printable)

        print("Password generated:")
        print(password)

    except:
        print("\nSomething unexpected went wrong  :( \n")
