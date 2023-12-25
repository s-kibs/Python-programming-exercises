# Write a program which accepts a sequence of comma separated 4 digit binary
# numbers as its input and then check whether they are divisible by 5 or 
# not. The numbers that are divisible by 5 are to be printed in a comma 
# separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
baseStr = input('Enter binary no.: ')
ans=[]
numSeq = [int(i,2) for i in baseStr.split(',')]

for i in numSeq:
        if i%5==0:
                ans.append(bin(i).replace('0b',''))

print(*ans, sep=',')