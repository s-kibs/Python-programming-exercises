# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class twoMethods:
    def __init__(self):
        self.Str1= ''
        pass
    def inString(self):
        self.Str1 = input('Enter a String: ')
    def outString(self):
        print(self.Str1.upper())
obj = twoMethods()
obj.inString()
obj.outString()