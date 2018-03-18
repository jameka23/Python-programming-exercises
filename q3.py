# Question:
# With a given integral number n, write a program to generate a dictionary
# that contains (i, i*i) such that is an integral number between 1 and n
# (both included). and then the program should print the dictionary.


def dict_gen(x):
    dictGen ={ }
    for i in range(1,x+1):
        dictGen[i] = [i*i]
    for k,v in dictGen.items():
        print("{}:{}".format(k,v))
        
i = int(raw_input())
dict_gen(i)
