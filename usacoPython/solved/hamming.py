#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   11/1/2022
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

# function below borrowed from geeksforgeeks.com
def hammingDistance(n1, n2) :
    # clever xor usage to get only different bits
    x = n1 ^ n2
    setBits = 0
    while (x > 0) :
        # bitshift through xor to find all 1s, total them
        setBits += x & 1
        x >>= 1
    return setBits

# declare globals
N = 0
B = 0
D = 0
maxSize = 0
maximum = 0
history = []

def solve(depth, last):
    # import globals and set current value to last found value
    global N, B, D, maxSize, maximum, history
    current = last
    while current < maxSize:
        for i in history:
            if hammingDistance(current, i) < D:
                break
        # solution IS found; the break statement is never encountered
        else: 
            # send through loop again if solution is not long enough
            history.append(current)
            if len(history) >= N:
                return
            solve(depth+1, current)
            # exit out of all recursion once a solution is found
            if len(history) >= N:
                return
            history.pop()
        current +=1
    return
       
# python equivalent of java nextInt function, returns next integer in input file when called
def nextInt():
    for line in open("hamming.in"):
         yield from (int(i) for i in line.split())

def main():
    global N, B, D, maxSize, maximum, history
    # read in input data
    infile = nextInt()
    N = next(infile)
    B = next(infile)
    D = next(infile)
    maxSize = 2**B
    # solve starting from depth 0 with starting value of 0
    solve(0, 0)
    # output data and exit program
    outfile = open("hamming.out", 'w')
    for i in range(len(history)):
        outfile.write(str(history[i])+ ("\n" if i%10==9 or i == len(history)-1 else " "))
    outfile.close()
    exit()
main()

 