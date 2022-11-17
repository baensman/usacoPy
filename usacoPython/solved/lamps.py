#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   11/12/2022
#  PROBLEM ID                  :   USACO - Party Lamps
#  PROBLEM DESCRIPTION         :   Find all possible ending states of a boolean array after
#                              :   C operations and set final states for certain indexes
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   N/A

'''
ID: basscla1
LANG: PYTHON3 
TASK: lamps
'''

# function to repeat a string to a given number of characters (courtesy of zwol on stackoverflow)
def repeat_to_length(s, wanted):

    # make string long enough to contain target length, and truncate from there
    return (s * (wanted//len(s) + 1))[:wanted] + "\n"

# python equivalent of java nextInt function, returns next integer in input file when called
def nextInt():
    for line in open("lamps.in"):
         yield from (int(i) for i in line.split())

def main():
    # read in input data
    infile = nextInt()
    N = next(infile)
    C = next(infile)

    # declare variables to traverse button graph
    ind = ["111111", "000000", "101010", "010101", "100100", "011011", "110001", "001110"]
    accepted = []
    possible = {0}
    traverse = [[1, 2, 3, 5], [0, 2, 3, 4], [0, 1, 3, 6], [0, 1, 2, 7], [1, 5, 6, 7], [0, 4, 6, 7], [7, 5, 2, 3], [6, 4, 2, 3]]

    # traverse array C times, if C > 3 then only 3 times necessary
    for i in range(C if C <= 3 else 3):
        temp = set(())
        for j in possible:
            temp.update(traverse[j]) 
        possible = temp
    
    # create array of possible results
    for i in possible:
        accepted.append(ind[i]) 
    a = accepted[:]

    # check for all invalid zeros
    read = next(infile)-1
    while read != -2:
        read %= 6
        for item in a:
            if item[read] != '1': 
                if item in accepted: accepted.remove(item)
        read = next(infile)-1

    # check for all invalid ones
    read = next(infile)-1
    while read != -2:
        read %= 6
        for item in a:
            if item[read] != '0': 
                if item in accepted: accepted.remove(item)
        read = next(infile)-1

    # output data multiplied to length N, impossible if no answers
    outfile = open("lamps.out", 'w')
    if len(accepted) == 0:
        outfile.write("IMPOSSIBLE\n")
    else:
        accepted.sort()
        for i in accepted:
            outfile.write(repeat_to_length(i, N))
    
    # close output file and exit
    outfile.close()
    exit()
main()

 
