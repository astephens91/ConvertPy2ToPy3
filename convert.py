# a program to count the number of vowels in a sentence.
# Painfully (and badly) written in python2.

import sys

result = input('Enter your phrase: ')
if not isinstance(result, str):
    traceback = sys.exc_info()[2]
    raise ValueError("Somehow you didn't enter a string."
                     "Please try again.").with_traceback(traceback)

try:
    result = int(result)
    print("That's not a string, that's a number. >_<")
    sys.exit()
except ValueError:
    # we want this to trigger
    pass

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_dict = dict()

for char in result:
    if char in vowels:
        vdc = int(vowel_dict.get(char, 0))
        vowel_dict[char] = vdc + 1

print("The total is: ")

for v, c in vowel_dict.items():
    print("{}: {} instances".format(v, c))
