# Question 5
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class Stringy(object):

    def __init__(self):
        self.the_string = ""
        
    def getString(self):
        self.the_string = input('Enter name:')
    
    def printString(self):
        print(self.the_string.upper())        


stuffy = Stringy()
name = stuffy.getString()

stuffy.printString()
