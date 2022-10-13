#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   10/13/2022
#  PROBLEM ID                  :   USACO - Hamming Codes
#  PROBLEM DESCRIPTION         :   Find N minimum values up  to bit length B 
#                              :   that are at least D hamming distance from each other
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   N/A

'''
ID: basscla1
LANG: PYTHON3 
TASK: hamming
'''

def nextBinary(reset):
    global B
    for i in range(2**B):
        if reset:
            i = 0
        yield bin(i)

from scipy.spatial.distance import hamming

N = 0
B = 0
D = 0
       
# python equivalent of java nextInt function, returns next integer in input file when called
def nextInt():
    for line in open("hamming.in"):
         yield from (int(i) for i in line.split())

def main():
    
    global N, B, D
    # read in input data
    infile = nextInt()
    N = next(infile)
    B = next(infile)
    D = next(infile)

    for ()
    # output data and exit program
    outfile = open("hamming.out", 'w')
    
    exit()
main()

 