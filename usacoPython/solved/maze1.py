#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   12/2/2022
#  PROBLEM ID                  :   USACO - Overfencing
#  PROBLEM DESCRIPTION         :   Find the point in a maze that is furthest from the exits
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   N/A

'''
ID: basscla1
LANG: PYTHON3 
TASK: maze1
'''


def main():
    # declare vars and input data
    infile = open("maze1.in", "r") 
    data = infile.readlines()
    nums = data[0].split()
    W = int(nums[0])
    H = int(nums[1])
    entrances = []
    key = [[0]*W for p in range(H)]
    solution = []
    sol = 1

    # construct array denoting where all walls occur giving each cell a value between 0 and 15
    # adding 1 represents a north wall, 2 = east, 4 = south, 8 = west
    for i in range(H):
        for j in range(W): 
            key[i][j] = (1 if data[2*i+1][2*j+1] == "-" else 0) + (2 if data[2*i+2][2*j+2] == "|" else 0) + (4 if data[2*i+3][2*j+1] == "-" else 0) + (8 if data[2*i+2][2*j] == "|" else 0)

            # check if entrances to the maze occur at the given index; add to entrances array
            if i == 0 and data[2*i+1][2*j+1] == " ":
                entrances.append([i, j])
                
            if j == 0 and data[2*i+2][2*j] == " ":
                entrances.append([i, j])
               
            if j == W-1 and data[2*i+2][2*j+2] == " ":
                entrances.append([i, j])
                
            if i == H-1 and data[2*i+3][2*j+1] == " ":
                entrances.append([i, j])

    # checking each entrance (only 2 in this problem) map all the distances to each array cell
    for start in entrances:

        # declare vars used for mapping
        boxes = [start] 
        walked = [[False] * W for p in range(H)]
        distances = [[1] * W for p in range(H)]
        walked[start[0]][start[1]] = True
        dist = 1

        # while there are boxes that can still be accessed, check for open boxes adjacent to those
        while len(boxes) > 0:
            dist+=1
            nextBoxes = set(())

            # check each box for adjacent open boxes; add to nextBoxes if so
            for box in boxes:
                i = box[0]
                j = box[1]
                temp = bin(key[i][j])[2:]
                if key[i][j] < 8:
                    temp = "0" + temp 
                if key[i][j] < 4:
                    temp = "0" + temp
                if key[i][j] < 2:
                    temp = "0" + temp
                if j != 0 and not walked[i][j-1] and temp[0] == "0":
                    walked[i][j-1] = True
                    nextBoxes.add((i,j-1))
                    distances[i][j-1] = dist
                if i != H - 1 and not walked[i+1][j] and temp[1] == "0":
                    walked[i+1][j] = True
                    nextBoxes.add((i+1,j))
                    distances[i+1][j] = dist
                if j != W-1 and not walked[i][j+1] and temp[2] == "0":
                    walked[i][j+1] = True
                    nextBoxes.add((i,j+1))
                    distances[i][j+1] = dist
                if  i != 0 and not walked[i-1][j] and temp[3] == "0":
                    walked[i-1][j] = True
                    nextBoxes.add((i-1,j))
                    distances[i-1][j] = dist
            boxes = [*nextBoxes][:]
        solution.append(distances)
            
    # find largest distance by finding the minimum distance to reach each cell and maximizing
    for i in range(H): 
        for j in range(W):
            if min(solution[0][i][j], solution[1][i][j]) > sol:
                sol = min(solution[0][i][j], solution[1][i][j])

    # output solution and close
    outfile = open("maze1.out", "w") 
    outfile.write(str(sol) + "\n")
    outfile.close()
    exit()
main()

 
