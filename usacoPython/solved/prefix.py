#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   11/16/2022
#  PROBLEM ID                  :   USACO - Longest Prefix
#  PROBLEM DESCRIPTION         :   Find all possible ending states of a boolean array after
#                              :   C operations and set final states for certain indexes
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   Kenneth Seybold, Prakash Shekhar

'''
ID: basscla1
LANG: PYTHON3 
TASK: prefix
'''

def main():
    # declare vars and read in input data
    infile = open("prefix.in", "r")
    bits = [] 
    S = ""
    ind = 1
    isReachable = [False]*200000 
    while True:
        temp = infile.readline().split()
        if "." in temp: break 
        bits += temp
    bits.sort(reverse=True, key=len)
    a = infile.readlines()
    for i in a:
        i = i[:-1]
        S+=i

    # set default case for beginning of sequence
    for bit in bits:
        if bit == S[0:len(bit)]:
            isReachable[len(bit)-1] = True

    # if no match at beginning, exit with default case
    if True not in isReachable:
        open("prefix.out", "w").write("0\n") 
        exit() 

    # iterate through string checking for what matches at each position
    while True:

        # if the current position isn't a reachable position, move to 
        # next reachable position; if none exist, then solution is found
        if not isReachable[ind-1]:
            if True not in isReachable[ind:ind+11]:
                break
            ind+=1
            continue 

        # check each bit for a match at the current position
        lastlen = 0
        for bit in bits:

            # if the current bit is the same length as the last, skip
            if len(bit) == lastlen:
                continue

            # mark the position in the reachable array 
            if bit == S[ind:len(bit)+ind]:
                isReachable[ind+len(bit)-1] = True
                lastlen = len(bit)
        ind+=1

    # find the last reachable position and output index
    isReachable.reverse()
    outfile = open("prefix.out", "w") 
    outfile.write(str(len(isReachable) - isReachable.index(True)) + "\n")

    # close output file and exit
    outfile.close()
    exit()
main()

 
