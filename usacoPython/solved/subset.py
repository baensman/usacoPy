#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   11/8/2022
#  PROBLEM ID                  :   USACO - Subset Sums
#  PROBLEM DESCRIPTION         :   Calculate number of ways to partition a set of numbers
#                              :   into two equal sum subsets
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   N/A

'''
ID: basscla1
LANG: PYTHON3 
TASK: subset
'''

# python equivalent of java nextInt function, returns next integer in input file when called
def nextInt():
    for line in open("subset.in"):
         yield from (int(i) for i in line.split())

def main():
    # read in input data
    infile = nextInt()
    N = next(infile)
    # if subsets would never sum to be equal, exit
    if sum([x for x in range(1, N+1)])%2 != 0:
        open("subset.out", "w").write("0\n")
        exit()
    
    # dp buckets solution by looking at number of ways to contruct a past subset 
    dp = [0] * (400)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N+1):
        dupe = dp[:]
        for j in range(i):
            dp.insert(0, 0)
            dp.pop()
        dupe = [sum(x) for x in zip(dupe, dp)]
        dp = dupe[:]

    # output max combination and exit
    outfile = open("subset.out", 'w')
    outfile.write(str(max(dp)//2) + "\n")
    outfile.close()
    exit()
main()

 