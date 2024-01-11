# Write a program that accepts a sentence and calculate the number of
# letters and digits. Suppose the following input is supplied to the
# program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# using variables
s = input("Enter input: ")
countNumber = 0
countLetter = 0
for i in s:
    if i.isdigit() :
        countNumber = countNumber + 1
    elif i.isalpha():
        countLetter = countLetter + 1
print('LETTERS' , countLetter)
print('DIGITS', countNumber)

# using dictionary
# s = input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print ("LETTERS", d["LETTERS"])
# print ("DIGITS", d["DIGITS"])