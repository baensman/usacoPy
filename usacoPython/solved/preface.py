#  NAME                        :   Lucas Oeming
#  GROUP                       :   APCS
#  LAST MODIFICATION DATE      :   11/1/2022
#  PROBLEM ID                  :   USACO - Preface Numbering
#  PROBLEM DESCRIPTION         :   Calculate total occurences of each roman numeral character
#                              :   given roman numerals between 1 and N
#  PEOPLE WHO I HELPED         :   N/A
#  PEOPLE WHO HELPED ME        :   N/A

'''
ID: basscla1
LANG: PYTHON3 
TASK: preface
'''

# python equivalent of java nextInt function, returns next integer in input file when called
def nextInt():
    for line in open("preface.in"):
         yield from (int(i) for i in line.split())

def main():
    # read in input data
    infile = nextInt()
    N = next(infile)
    I = [0, 1, 3, 6, 7, 7, 8, 10, 13, 14, 0]
    V = [0, 0, 0, 0, 1, 2, 3, 4, 5, 5]
    X = [0, 1, 2, 3, 1, 0, 1, 2, 3, 1]
    outfile = open("preface.out", 'w')

    # each str() statement below calculates the number of occurences of that letter given any number up to 3500
    # a lot of trial and error/code bandaids are present but it gets the job done somehow
    # feel free to try to decipher what is happening in C and M
    outfile.write("I " + str(I[N%5]+7*(N//5)) + "\n")
    if N < 4: exit()
    outfile.write("V " + str(V[N%10]+5*(N//10)) + "\n")
    if N < 9: exit()
    outfile.write("X " + str(150*(N//100) + (N%10+1)*X[(N%50)//10] + I[(N%100)//10-1]*10 + ((N%100)+1)//10) + "\n")
    if N < 40: exit()
    outfile.write("L " + str(50*(N//100) + min(50, max(0, (N%100-39)) ) ) + "\n")
    if N < 90: exit()
    outfile.write("C " + str(1500*(N//1000) + (N%100+1)*X[(N%500)//100] + I[(N%1000)//100-1]*100 + ((N%1000)//100)*10 + (1 + (N+10)%100 if (N+10)%100 < 10 else 0)) + "\n")
    if N < 400: exit()
    outfile.write("D " + str(500*(N//1000) + min(500, max(0, (N%1000-399)) ) ) + "\n")
    if N  < 900: exit()
    outfile.write("M " + str((N%1000+1)*X[(N)//1000] + I[(N)//1000-1]*1000 + ((N)//1000)*100 + (1 + (N+100)%1000 if (N+100)%1000 < 100 else 0)) + "\n")
    outfile.close()
    exit()
main()

 