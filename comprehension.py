# The program generate a random number between 1 and 20 and the user has 6 try to guess it. 


import random  # make it possible to access to the code in the random module

guessesTaken = 0  # Assign 0 to guessesTaken variable

print('Hello! What is your name?')  # The string 'Hello! What is your name?' is written to the standard output
                                    # and a newline character added at the end by default.


myName = input()  # waiting for an input to read in till user press Enter, assign the typed string value to myName variable

number = random.randint(1, 20)  # generate a random integer between 1 and 20 (1 and 20 included) and assign it to number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # First,print() function merge the three strings into a single object temporarily
#  then write it to the standard output (terminal) and a newline character added at the end by default.

while guessesTaken < 6:  # The loop will be repeated until value stored in guessesTaken variable less than 6:
    print('Take a guess.')  # Inside the loop: The string 'Take a guess.' and a newline character are written out.
    guess = input()                         # waiting for an input to read in till user press Enter, assign the typed string to guess variable
    guess = int(guess)                      # convert the value stored in guess variable(originally string type) into an integer

    guessesTaken += 1                       # increase guessesTaken value by one

    if guess < number:                      # if the condition is true (value stored in guess variable smaller than value stored in number variable) then 
        print('Your guess is too low.')     # the string 'Your guess is too low.' and a newline character are written out.

    if guess > number:                      # if value stored in guess variable larger than value stored in number variable then 
        print('Your guess is too high.')    # the string 'Your guess is too high.' and a newline character are written out.

    if guess == number:                     # if value stored in guess variable equal to value stored in number variable then 
        break                               # break immediately terminates the current loop and resumes execution at the next statement.

if guess == number:                         # if value stored in guess variable equal to value stored in number variable then 
    guessesTaken = str(guessesTaken)        # convert the value stored in guessesTaken variable(originally integer type) into a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # print() function temporarily merge the five strings into a single object then 
                                                                                                #writes it out and add a newline.
if guess != number:                         # if the condition is false (value stored in guess variable not equal to value stored in number variable) then 
    number = str(number)                    # convert the value stored in number variable(originally integer type) into a string
    print('Nope. The number I was thinking of was ' + number)  # print() function merge the two strings into a single object temporarily then writes it out to terminal and add a newline
