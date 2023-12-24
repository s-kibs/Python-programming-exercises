# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

startNumber = 2000

for startNumber in range(startNumber, 3201):
    if startNumber % 7 == 0 and startNumber % 5 != 0:
        print(startNumber, end=",")
