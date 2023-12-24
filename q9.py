# Write a program that accepts sequence of lines as input and prints the lines 
# after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

strLines= []

while True:
    userInput = input()
    if userInput == '':
        break
    else:
        strLines.append(userInput.upper() + '\n')
print(''.join(strLines))