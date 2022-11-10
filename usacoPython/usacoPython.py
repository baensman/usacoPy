#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   11/10/2022
#  PROBLEM ID                  :   USACO - Party Lamps
#  PROBLEM DESCRIPTION         :   Find all possible ending states of a boolean array after
#                              :   C operations and set final states for certain indexes
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   N/A

'''
ID: basscla1
LANG: PYTHON3 
TASK: party
'''
oddsum = 0
evensum = 0
def buttonOne(current):
    return ~current

def buttonTwo(current):
    return 
# python equivalent of java nextInt function, returns next integer in input file when called
def nextInt():
    for line in open("runround.in"):
         yield from (int(i) for i in line.split())

def main():
    # read in input data
    infile = nextInt()
    N = next(infile)
    C = next(infile)
    oddsum = sum([2**x for x in range(0, N, 2)])
    final = [0]*N
    read = next(infile)
    while read != -1:
        final[read] = 2
    read = next(infile)
    while read != -1:
        final[read] = 1
    
    # output next runaround and close
    outfile = open("runround.out", 'w')
    outfile.write(str(M) + "\n")
    outfile.close()
    exit()
main()

 
