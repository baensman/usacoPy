#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   11/30/2022
#  PROBLEM ID                  :   USACO - Controlling Companies
#  PROBLEM DESCRIPTION         :   Find all pairs of companies that control each other
#                              :   given the percentages of control between all companies
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   Jon Jalozynski

'''
ID: basscla1
LANG: PYTHON3 
TASK: concom
'''
     
# python equivalent of java nextInt function, returns next integer in input file when called
def nextInt():
    for line in open("concom.in", "r"):
         yield from (int(i) for i in line.split())
    
def main():
    # declare vars and input data
    infile = nextInt() 
    outfile = open("concom.out", "w")
    N = next(infile) 
    data = [[0]*100 for i in range(100)] 
    comps = []
    comp = set(())
    for q in range(N):
        i = next(infile)
        j = next(infile)
        comp.add(i-1)
        comp.add(j-1)
        p = next(infile)
        data[i-1][j-1] = p/100

    # store all valid companies into an ordered list
    comps = [*comp]

    # start with each company as a root node
    for i in comps: 

        # initialize default of no companies controlled and original percentages of control
        control = data[:]
        isControlled = [[False]*100 for i in range(100)]
        
        # check for a new company that can be controlled, loop through all companies each time
        # until no new companies found
        while True: 
            for j in comps: 
                if j == i: continue
                if not isControlled[i][j] and control[i][j] >= 0.5: 
                    isControlled[i][j] = True 
                    control[i] = [sum(tup) for tup in zip(control[i], control[j])]
                    break
            else:
                break

        # output all companies controlled by company i
        for j in comps:
            if isControlled[i][j]:
                    outfile.write(str(i+1) + " " + str(j+1) + "\n")

    # close output file
    outfile.close()
    exit()
main()

 
