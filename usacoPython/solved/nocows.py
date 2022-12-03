#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   11/30/2022
#  PROBLEM ID                  :   USACO - Cow Pedigrees
#  PROBLEM DESCRIPTION         :   Find all combinations of a binary tree with
#                              :   N nodes, where any node can have 0 or 2 children.
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   Coding with Dong, Prakash Shekar, Kenny Seybold

'''
ID: basscla1
LANG: PYTHON3 
TASK: nocows
'''
     
# python equivalent of java nextInt function, returns next integer in input file when called
def nextInt():
    for line in open("nocows.in", "r"):
         yield from (int(i) for i in line.split())

def main():

    # declare vars and input data; initialize dp base case
    infile = nextInt() 
    outfile = open("nocows.out", "w")
    N = next(infile)
    K = next(infile)
    data = [([0]+[1]*100 if p == 1 else [0]*101) for p in range(202)]

    # case where number of nodes is even (impossible)
    if N % 2 == 0 or K == 0:
        outfile.write("0\n")
        exit()

    # j = number of nodes, i = current depth
    # solution keeps track of number of combinations UP TO THE CURRENT INDEX
    # solver only looks at last row ans multiplies ways to make different pairs add to
    # target number of nodes by adding to a root node (ex. 11 can be split into 1+[9+1,7+3,5+5])
    for j in range(1, N+1, 2):
        for i in range(1, K+1):
            for ind in range(1, j, 2):
                data[j][i] += data[ind][i-1] * data[j-ind-1][i-1] 

    # output data and exit program, remove last number of solutions to only get the target depth
    outfile.write(str((data[N][K]-data[N][K-1]+9901)%9901) + "\n")
    outfile.close()
    exit()
main()

 
