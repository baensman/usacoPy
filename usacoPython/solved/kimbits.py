#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   2023-05-13
#  PROBLEM ID                  :   USACO - Stringsobits
#  PROBLEM DESCRIPTION         :   Find the nth term of an ordered set of binary strings of length N
#                              :   containing up to L "1" bits
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   Levi Scranton

'''
ID: basscla1
LANG: PYTHON3 
TASK: kimbits
'''

from math import comb


# python equivalent of java nextInt function, returns next integer in input file when called
def nextInt():
    for line in open("kimbits.in", "r"):
         yield from (int(i) for i in line.split())

# recursively pick ones or zeros to add on to built string based on whether the amount of permutations still needed fits
# in the remaining bits
def solve(n, l ,i):
    if n == 0: return ""
    s = sum([comb(n-1, x) for x in range(0, l+1)])
    if s >= i:
        return "0" + solve(n-1, l, i)
    else:
        return "1" + solve(n-1, l-1, i-s)

def main():
    # declare vars and input data
    infile = nextInt() 
    N = next(infile) 
    L = next(infile) 
    I = next(infile) 

    # output picked out solution
    open("kimbits.out", "w").write(solve(N, L, I) + "\n")
    exit()
main()

 
