#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   11/30/2022
#  PROBLEM ID                  :   USACO - The Tamworth Two
#  PROBLEM DESCRIPTION         :   Find the time it will take for two players to meet if
#                              :   they traverse a graph moving forward or turning clockwise
#                              :   if there is an obstacle in front of them
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   N/A

'''
ID: basscla1
LANG: PYTHON3 
TASK: ttwo
'''
    
def main():
    # declare vars and input data
    isObstacle = [[True]*12 for p in range(12)]
    data = open("ttwo.in", "r").readlines() 
    fhistory = []
    chistory = []
    mins = 0

    # set array of obstacles and initialize positions of farmer + cows
    for i in range(10):
        for j in range(10):
            if data[i][j] == ".":
                isObstacle[i+1][j+1] = False
            if data[i][j] == "F":
                farmer = [i+1, j+1, 0]
                isObstacle[i+1][j+1] = False
            elif data[i][j] == "C":
                cows = [i+1, j+1, 0]
                isObstacle[i+1][j+1] = False

    # while the positions aren't equal perform movements
    while cows[0] != farmer[0] or cows[1] != farmer[1]:
        mins+=1
        if farmer[2] == 0:
            if isObstacle[farmer[0]-1][farmer[1]]:
                farmer[2] = (farmer[2]+1)%4
            else: 
                farmer[0]-=1
        elif farmer[2] == 1:
            if isObstacle[farmer[0]][farmer[1]+1]:
                farmer[2] = (farmer[2]+1)%4
            else: 
                farmer[1]+=1
        elif farmer[2] == 2:
            if isObstacle[farmer[0]+1][farmer[1]]:
                farmer[2] = (farmer[2]+1)%4
            else: 
                farmer[0]+=1
        elif farmer[2] == 3:
            if isObstacle[farmer[0]][farmer[1]-1]:
                farmer[2] = (farmer[2]+1)%4
            else: 
                farmer[1]-=1
        if cows[2] == 0:
            if isObstacle[cows[0]-1][cows[1]]:
                cows[2] = (cows[2]+1)%4
            else: 
                cows[0]-=1
        elif cows[2] == 1:
            if isObstacle[cows[0]][cows[1]+1]:
                cows[2] = (cows[2]+1)%4
            else: 
                cows[1]+=1
        elif cows[2] == 2:
            if isObstacle[cows[0]+1][cows[1]]:
                cows[2] = (cows[2]+1)%4
            else: 
                cows[0]+=1
        elif cows[2] == 3:
            if isObstacle[cows[0]][cows[1]-1]:
                cows[2] = (cows[2]+1)%4
            else: 
                cows[1]-=1

        # check for repeats with unreasonably high amount of steps taken
        if cows in chistory and farmer in fhistory and mins > 10000:
            mins = 0
            break

        # add current state to history array to check for repeats later
        chistory.append(cows[:]) 
        fhistory.append(farmer[:])

    # open output file; output time taken to meet; close output file
    outfile = open("ttwo.out", "w")
    outfile.write(str(mins) + "\n")
    outfile.close()
    exit()
main()

 
