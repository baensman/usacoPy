#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   11/9/2022
#  PROBLEM ID                  :   USACO - Runaround Numbers
#  PROBLEM DESCRIPTION         :   Calculate the next smallest number in which 
#                              :   traversing all of the digits results in an infinite loop
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   N/A

'''
ID: basscla1
LANG: PYTHON3 
TASK: runround
'''

# python equivalent of java nextInt function, returns next integer in input file when called
def nextInt():
    for line in open("runround.in"):
         yield from (int(i) for i in line.split())

# function to check if a number is runaround
def isRunround(l, s):
    # default cases such as zeros, infinite single loopings, or duplicates
    if "0" in s :
        return s.index("0")
    if len(set(s)) != l:
        for j in s:
            if s.count(j) > 1:
                return s.index(j)

    # array of all infinite singles for a given length of number
    skips = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 4, 6, 8], [3, 6, 9], [4, 8], [5], [6], [7], [8], [9]]
    for i in skips[l-1]:
        if str(i) in s: 
            return s.index(str(i))

    # check manually for runaround number if no shortcuts found
    end = set(())
    i = 0
    for k in range(l):
        temp = i-int(s[i])%l 
        if temp < 0: temp +=l
        if temp in end:
            return 0
        end.add(temp)
        i = temp
    return -1

def main():
    # read in input data
    infile = nextInt()
    M = next(infile)+1
    S = (str(M))[::-1]
    L = len(S)

    # check initial case to see if next number is runaround
    check = isRunround(L, S)

    # function returns -1 if runround found, fix the problem digit if not runaround
    while check != -1:
        M += 10**check
        S = (str(M))[::-1]
        L = len(S)
        check = isRunround(L, S)
    
    # output next runaround and close
    outfile = open("runround.out", 'w')
    outfile.write(str(M) + "\n")
    outfile.close()
    exit()
main()

 