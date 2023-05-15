#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   2023-5-13
#  PROBLEM ID                  :   USACO Magic Square
#  PROBLEM DESCRIPTION         :   Find the transformations needed to reach a permutation of
#                              :   a Rubik's Magic Square.
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   N/A

'''
ID: basscla1
LANG: PYTHON3 
TASK: msquare
'''

def main():

    # declare dictionary and input data; set inital value
    seen = {}
    data= open("msquare.in", "r").readline().replace(" ", "")[:8]
    seen.update({"12345678":""})

    # calculate all 8! permutations using BFS based on the set of nodes previously calculated
    while len(seen) < 40320:
        for item in seen.copy():
            if not (x:=item[::-1]) in seen or (len(seen[item])+1 <= len(seen[x]) and seen[item]+"A" <= seen[x]): seen.update({x:seen[item]+"A"}) 
            if not (x:=item[3] + item[:3] + item[5:] + item[4]) in seen or (len(seen[item])+1 <= len(seen[x]) and seen[item]+"B" <= seen[x]): seen.update({x:seen[item]+"B"}) 
            if not (x:=item[0] + item[6] + item[1] + item[3] + item[4] + item[2] + item[5] + item[7]) in seen or (len(seen[item])+1 <= len(seen[x]) and seen[item]+"C" <= seen[x]): seen.update({x:seen[item]+"C"}) 

    # output minimum path at desired index and exit program
    open("msquare.out", "w").write(str(len(seen[data])) + "\n" + seen[data] + "\n")
    exit()
main()

 
