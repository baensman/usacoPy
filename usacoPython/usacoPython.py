#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   11/17/2022
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

# python equivalent of java nextInt function, returns next integer in input file when called
def nextInt():
    for line in open("zerosum.in", "r"):
         yield from (int(i) for i in line.split())

def main():
    # read in input data and declare vars
    infile = nextInt() 
    N = next(infile) 

    # open output file
    outfile = open("zerosum.out", "w")

    # close output file and exit
    outfile.write("\n")
    outfile.close()
    exit()
main()

 
