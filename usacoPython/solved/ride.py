'''
ID: basscla2
LANG: PYTHON3
TASK: ride
'''

import math

def main():
    infile = open("ride.in", "r")
    outfile = open("ride.out", "w")
    str = infile.read().splitlines()
    prodone = prodtwo = 1
    temp = ord(str[0][0])
    for i in str[0]:
        prodone *= ord(i)-64
    for i in str[1]:
        prodtwo *= ord(i)-64
    if prodone % 47 == prodtwo % 47:
        outfile.write("GO\n")
    else:
        outfile.write("STAY\n")
main()

