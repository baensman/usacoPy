#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   2023-5-13
#  PROBLEM ID                  :   USACO Feed Ratios
#  PROBLEM DESCRIPTION         :   Find the minimum integer solutions to a three dimensional system of equations
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   N/A

'''
ID: basscla1
LANG: PYTHON3 
TASK: ratios
'''

from math import gcd
seen = [[], []]
f = []
def solve(ratio, a, b, c):
    global seen, f
    if ratio in seen[0] or a == 100 or b == 100 or c == 100: return 
    seen.append([ratio, [a,b,c]])
    solve([ratio[x] + f[0][x] for x in range(3)], a+1,b,c)
    solve([ratio[x] + f[1][x] for x in range(3)], a,b+1,c)
    solve([ratio[x] + f[2][x] for x in range(3)], a,b,c+1)

def main():
    f = []
    # declare dictionary and input data; set inital value
    
    infile = open("ratios.in", "r") 
    goal = [int(x) for x in infile.readline().split()]
    check = [[x*i for x in goal] for i in range(1, 100)]
    for i in range(3):
        fthree = [int(x) for x in infile.readline().split()]
        f.append(fthree)
    sols = [] 
    current = [0, 0, 0]
    for i in range(100):
        current = [current[0] + i*f[0][0], current[1] + i*f[0][1], current[2] + i*f[0][2]]
        for j in range(100):
            current = [current[0] + j*f[1][0], current[1] + j*f[1][1], current[2] + j*f[1][2]]
            for k in range(100):
                r = [i,j,k] 
                #if gcd(*r) != 1 and 0 n: continue 
                current = [current[0] + f[2][0], current[1] + f[2][1], current[2] + f[2][2]]
                if current in check: 
                    sols.append([r, current])
                    break
                
            else:
                current = [current[0] - k*f[2][0], current[1] - k*f[2][1], current[2] - k*f[2][2]]
                current = [current[0] - j*f[1][0], current[1] - j*f[1][1], current[2] - j*f[1][2]]
                continue 
            break 
        else:
            current = [current[0] - i*f[0][0], current[1] - i*f[0][1], current[2] - i*f[0][2]]
            continue 
        break
    outfile = open("ratios.out", "w")
    if len(sols) == 0:
        outfile.write("NONE\n")
        exit()
    for i in sols[0][0]:
        outfile.write(str(i) + " ")
    outfile.write(str(gcd(*sols[0][1])) + "\n")
    exit()
main()

 
