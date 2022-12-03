#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   12/2/2022
#  PROBLEM ID                  :   USACO - Bessie Come Home
#  PROBLEM DESCRIPTION         :   Find the shortest possible path from a node to any
#                              :   other 'filled' node.
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   N/A

'''
ID: basscla1
LANG: PYTHON3 
TASK: comehome
'''

from json.encoder import INFINITY


def toDecimal(k):
    return ord(k) - (65 if k.isupper() else 71)


def main():
    # declare vars and input data
    infile = open("comehome.in", "r") 
    data = infile.readlines()[1:]
    dists = [[INFINITY]*52 for p in range(52)]
    vertices = set(())

    # create distances array with mirroring
    for line in data:
        temp = line.split()
        vertices.add(toDecimal(temp[0])) 
        vertices.add(toDecimal(temp[1])) 
        if int(temp[2]) < dists[toDecimal(temp[1])][toDecimal(temp[0])]:
            dists[toDecimal(temp[1])][toDecimal(temp[0])] = int(temp[2])
            dists[toDecimal(temp[0])][toDecimal(temp[1])] = int(temp[2])

    # Dijkstra's Algorithm 
    d = [INFINITY]*(max(vertices)+1)
    d[25] = 0 
    v = [False]*(max(vertices)+1)
    visited = set(())
    while len(visited) < len(vertices):
        mini = INFINITY
        for i in vertices:
            if v[i]: continue 
            if d[i] < mini:
                mini = d[i] 
                ind = i
        visited.add(ind)
        v[ind] = True 
        for j in range(max(vertices)+1):
            if dists[ind][j] == INFINITY or v[j]: continue
            if d[ind] + dists[ind][j] < d[j]:
                d[j] = d[ind] + dists[ind][j]

    # find smallest distance to an occupied field
    test = INFINITY
    for i in vertices:
        if i > 24: break 
        if d[i] < test:
            test = d[i]
            ind = i 

    # output solution and close
    outfile = open("comehome.out", "w") 
    outfile.write(chr(ind+65) + " " + str(test)  + "\n")
    outfile.close()
    exit()
main()

 
