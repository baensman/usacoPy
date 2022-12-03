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

def dist(one, two):
    return ((one[0]-two[0])**2 + (one[1]-two[1])**2)**0.5

def connected(matrix):
    for i in matrix:
        if True in i:
            start = i.index(True)
            break
    visited = set(())
    visited.add(start)
    while True: 
        l = len(visited)
        if l == len(matrix): 
            return True
        for k in visited.copy(): 
            indexes = [i for i, j in enumerate(matrix[k]) if j == True]
            visited.update(indexes) 
        if l == len(visited):
            return False




# python equivalent of java nextInt function, returns next integer in input file when called
def nextInt():
    for line in open("cowtour.in", "r"):
         yield from (int(i) for i in line.split())

def main():
    # declare vars and input data
    infile = open("cowtour.in", "r") 
    temp = nextInt()
    N = next(temp)
    matrix = []
    vertices = [] 
    for i in range(N):
        x = next(temp)
        y = next(temp)
        vertices.append([x,y])
    for bit in infile.readlines()[N+1:2*N+2]:
        temp = []
        for char in bit:
            if char == "\n": continue
            if char == "0":
                temp.append(False)
            else:
                temp.append(True) 
        matrix.append(temp)

    solutions = []
    for i in range(N): 
        for j in range(i, N):
            if matrix[i][j] == True or i == j: continue
            matrix[i][j] = True 
            matrix[j][i] = True
            if connected(matrix):
                distances = [[INFINITY]*N for p in range(N)]
                for I in range(N):
                    for J in range(N):
                        if I == J and not matrix[I][J]: continue
                        distances[I][J] = dist(vertices[I], vertices[J])
                for K in range(N): 
                    for I in range(N): 
                        for J in range(N): 
                            if distances[I][K] + distances[K][J] < distances[I][J]:
                                distances[I][J] = distances[I][K] + distances[K][J]
                max = 0
                for I in range(N): 
                    for J in distances[I]:
                        if J > max: max = J
                solutions.append(max)

            matrix[i][j] = False
            matrix[j][i] = False

    # output solution and close
    outfile = open("cowtour.out", "w") 
    outfile.write(str(min(solutions))  + "\n")
    outfile.close()
    exit()
main()

 
