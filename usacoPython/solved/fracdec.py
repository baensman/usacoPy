#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   12/1/2022
#  PROBLEM ID                  :   USACO - Fractions to Decimals
#  PROBLEM DESCRIPTION         :   Find the decimal equivalent of a fraction and find 
#                              :   any repetant terminating sequences
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   N/A

'''
ID: basscla1
LANG: PYTHON3 
TASK: fracdec
'''

import textwrap
from math import log10

# python equivalent of java nextInt
def nextInt():
    for line in open("fracdec.in", "r"):
         yield from (int(i) for i in line.split())
    
def main():
    # declare vars and input data
    infile = nextInt() 
    N = next(infile) 
    D = next(infile) 
    esc = False
    CHARS = 100000
    prefix = str(N//D) + "." 
    data = ""
    output = ""
    N %= D

    # check for case of power of ten denominator to avoid excess loopings
    if log10(D) == int(log10(D)):
        precision = int(log10(D))
        a = N/D
        open("fracdec.out", "w").write(f'{a:.{precision}f}' + "\n")
        exit()

    # create string of decimal places CHARS long
    for i in range(CHARS):
        N*=10
        data+=str(N//D)
        N %= D

    # look for repeatings strings by checking if both halvesa string split in half are equal,
    # and the next digit in the data string is equal to the first digit of the test string
    for i in range(CHARS-2):
        if esc:
            break
        for j in range(2, CHARS-i-2, 2):
            if data[i:i+j//2] == data[i+j//2:i+j] and data[i] == data[j+i]:
                temp = zip(data[i:], data[i:i+j//2]*2000)
                if all([x[0] == x[1] for x in temp]):

                    # if solution found, construct output and break loops
                    esc= True 
                    output = prefix
                    if data[i:i+j//2] != '0':
                        output += "(" + data[i:i+j//2] + ")"
                    if output[-1] == ".": output += "0"
                    break 
        else:
            prefix += data[i]
    
    # open output file; output formatted data; close output file
    outfile = open("fracdec.out", "w")
    output = textwrap.wrap((output), 76)
    for out in output:
        outfile.write(out + "\n")
    outfile.close()
    exit()
main()

 
