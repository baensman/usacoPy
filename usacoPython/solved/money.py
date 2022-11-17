#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   11/17/2022
#  PROBLEM ID                  :   USACO - Money Systems
#  PROBLEM DESCRIPTION         :   Find all ways to sum to a value given
#                              :   a set of primitives any any number of duplicates
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   Kenneth Seybold

'''
ID: basscla1
LANG: PYTHON3 
TASK: money
'''

# python equivalent of java nextInt function, returns next integer in input file when called
def nextInt():
    for line in open("money.in", "r"):
         yield from (int(i) for i in line.split())

def main():
    # read in input data and declare vars
    infile = nextInt() 
    V = next(infile) 
    N = next(infile) 
    coins = [next(infile) for i in range(V)]
    coins.sort()
    dp = [1] + [0]*30000

    # for each coin less than N find the number of ways to construct values above it by
    # adding the current number of ways to that index; 2 ways to make 2, add 5 coin = 2 ways to make 7
    for i in coins:
        if i > N: continue
        for j in range(N+1):
            dp[i+j] += dp[j] 

    # open output file
    outfile = open("money.out", "w")

    # close output file and exit
    outfile.write(str(dp[N])+"\n")
    outfile.close()
    exit()
main()

 
