# Write a program that accepts a sequence of whitespace separated words as 
# input and prints the words after removing all duplicate words and sorting 
# them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

rawInp = (input("Enter Input: "))
newList = [n for n in rawInp.split(' ')]
tempList = []
[tempList.append(i) for i in newList if i not in tempList]
tempList.sort()
print(' '.join(tempList))

