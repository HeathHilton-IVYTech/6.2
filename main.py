# Heath Hilton
# 11/06/2022

# Program: 6.2 - Guess my number

# The program is going to slowly guess a number
guess_me = 7
number = 1

while number != guess_me:
    if number < guess_me:
        print("too low")
        number += 1
    else:
        print("oops")
        break
else:
    print("found it!")