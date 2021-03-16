# This will read a random Mad Lib
import random

# Opens the text file
f = open('madlibs.txt', 'r')

# Reads the whole file and stores it in a list
madlibText = f.readlines()

# Choose a random line from that list
madlib = random.choice(madlibText)

# Shows the users what the text will be
print(madlib)

# Ask the user to write a noun
noun = input("Enter a noun: ")

# Replace the blank with the users input
madlib = madlib.replace("blank", noun)

# Print out the madlib with the users noun
print(madlib)
