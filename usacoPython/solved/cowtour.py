#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   12/2/2022
#  PROBLEM ID                  :   USACO - Cow Tours
#  PROBLEM DESCRIPTION         :   Find the best way to connect two graphs in order to keep
#                              :   the graph diamater to a minimum
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   N/A

'''
ID: basscla1
LANG: PYTHON3 
TASK: cowtour
'''

from math import inf, dist


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
        
    pasone = set(())
    for i in matrix:
        if True in i:
            pasone.add(i.index(True))
            break
    else:
        solution = min([dist(vertices[p], vertices[p+1]) for p in range(N-1)])
        outfile = open("cowtour.out", "w") 
        outfile.write("{:.6f}".format(round(solution, 6)) + "\n")
        outfile.close()
        exit()
    while True: 
        l = len(pasone)
        for k in pasone.copy(): 
            indexes = [i for i, j in enumerate(matrix[k]) if j == True]
            pasone.update(indexes) 
        if l == len(pasone):
            break
    pastwo = set(()) 
    for i in range(N):
        if i not in pasone:
            pastwo.add(i)

    distances = [[inf]*N for p in range(N)]
    for I in range(N):
        for J in range(N):
            if I == J:
                distances[I][J] = 0
                continue 
            elif not matrix[I][J]: continue
            distances[I][J] = dist(vertices[I], vertices[J])
    for K in range(N): 
        for I in range(N): 
            if I == K: continue
            for J in range(N): 
                if I == J or J == K:
                    continue
                if distances[I][K] + distances[K][J] < distances[I][J]:
                    distances[I][J] = distances[I][K] + distances[K][J]
    for I in range(N):
        for J in range(N):
            if distances[I][J] == inf:
                distances[I][J] = 0

    solutions = []
    for i in pastwo: 
        for j in pasone:
            if matrix[i][j]: continue
            #print(str(i) + "  " + str(j) + "  " + str(max(distances[i])) + "  " + str(dist(vertices[i], vertices[j])) + "  " + str(max(distances[j])) + " =   " + str(max(distances[i]) + dist(vertices[i], vertices[j]) + max(distances[j])))
            solutions.append(max(distances[i]) + dist(vertices[i], vertices[j]) + max(distances[j]))


    # output solution and close
    outfile = open("cowtour.out", "w") 
    outfile.write("{:.6f}".format(round(min(solutions), 6)) + "\n")
    outfile.close()
    exit()
main()

 
