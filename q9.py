# Write a program that accepts sequence of lines as input and
# prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT


#lines = [x for x in input("Enter lines: ").split(',')]

#for line in lines:
#    print(line.upper())


liness = []
while True:
    s = input("enter")
    if s:
        liness.append(s.upper())
    else:
        break

for sentence in liness:
    print(sentence)
