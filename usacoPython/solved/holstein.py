'''
ID: basscla2
LANG: PYTHON3 
TASK: holstein
'''

import itertools

V = 0
cowReqs = []
feeds = [] 
G = 0
best = [25] * 25

# list element-wise addition function ([1,2] + [3,4] = [4,6])
def add(list1, list2):
    out = []
    for i in range(len(list1)):
        out.append(list1[i] + list2[i])
    return out
    
# declare solve function
def solve():

    # access global variables
    global G
    global V
    global best
    global feeds
    global cowReqs

    # generate all possible index combinations of feeds and test to see if it meets reqs.
    for i in range(V+1, 0, -1):
        for sub in itertools.combinations([a for a in range(G)], i):
            test = [0]*V 
            for indx in sub:
                test = add(test, feeds[indx]) 
            works = True
            for l in range(V):
                if test[l] < cowReqs[l]:
                    works = False
                    break
            if works:
                best = sub[:]
                break
       
# python equivalent of java nextInt function, returns next integer in input file when called
def nextInt():
    for line in open("holstein.in"):
         yield from (int(i) for i in line.split())

def main():

    # access global variables
    global maxDepth
    global G
    global V
    global best
    global feeds
    global cowReqs

    # read in input data
    infile = nextInt()
    V = next(infile)
    maxDepth = V
    for i in range(V):
        cowReqs.append(next(infile))
    G = next(infile)
    for i in range(G):
        feeds.append([])
        for j in range(V):
            feeds[i].append(next(infile))

    # run solve function
    solve()

    # output data and exit program
    outfile = open("holstein.out", 'w')
    outfile.write(str(len(best)) + " ")
    for i in best:
        if i != best[-1]:
            outfile.write(str(i+1) + " ")
        else:
            outfile.write(str(i+1))
    outfile.write("\n")
    exit()
main()

 