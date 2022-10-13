'''
ID: basscla2
LANG: PYTHON3
TASK: friday
'''


def main():
    infile = open("friday.in", "r")
    outfile = open("friday.out", "w")
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekday = 0 
    thirteenths = [0, 0, 0, 0, 0, 0, 0]
    WEEK_LENGTH = 7
    for i in range(1900, (int(infile.read())+1900)):
        if i % 400 == 0 or i % 4 == 0 and i % 100 != 0:
            months[1] = 29
        else:
            months[1] = 28
        for j in range(12):
            thirteenths[weekday%WEEK_LENGTH]+=1
            weekday += months[j]
    for i in range(6):
        outfile.write(str(thirteenths[i]) + " ")
    outfile.write(str(thirteenths[6]) + "\n")

    infile.close()
    outfile.close()
main()

