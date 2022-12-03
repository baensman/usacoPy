#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   11/18/2022
#  PROBLEM ID                  :   USACO - Zero Sum
#  PROBLEM DESCRIPTION         :   Find all ways to sum to zero given a list
#                              :   of integers (3-9) and possible operations of
#                              :   adding, subtracting, or combining digits
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   N/A

'''
ID: basscla1
LANG: PYTHON3 
TASK: zerosum
'''

# declare globals
N = 0
sols = []
history = []

# function to store formatted solutions in array
def returnSolution():
     global history
     s = ""
     for b in history:
         s += ("+" if b > 0 and b != 1 and b != 10 else "") + str(b)
     
     # deal with zeros from powers of ten
     s = s.replace("0-", " ")
     s = s.replace("0+", " ")   
     sols.append(s+"\n")
     
# define recursive function 
def solve(canLink, sum, add, depth, sign):

     # set variables
     global N, history
     history.append(add) 
     sum+=add

     # if the end has been reached, check for zero sum and store if true
     if depth == N+1:
         if sum == 0:
             returnSolution()
         history.pop()
         return 

     # check if current position can contain a combining character
     if canLink: 

         # don't combine characters if there is nothing to combine with
         if depth != N:
            solve(False, sum, 10*depth*sign, depth+1, 1) 
            solve(False, sum, -10*depth*sign, depth+1, -1)
         solve(True, sum, depth, depth+1, 1)
         solve(True, sum, -depth, depth+1, 1)
     else: 
         solve(True, sum, depth*sign, depth+1, 1)
     history.pop()
     return
     
# python equivalent of java nextInt function, returns next integer in input file when called
def nextInt():
    for line in open("zerosum.in", "r"):
         yield from (int(i) for i in line.split())

def main():

    # read in input data and declare vars
    global N, sols
    infile = nextInt() 
    N = next(infile) 

    # solve with starting possibilities of 1 or 10
    solve(True, 0, 1, 2, 1)
    solve(False, 0, 10, 2, 1)
    # output data and exit program
    sols.sort()
    outfile = open("zerosum.out", "w")
    for j in sols:
        outfile.write(j)
    outfile.close()
    exit()
main()

 
