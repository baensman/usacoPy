'''
ID: basscla2
LANG: PYTHON3
TASK: gift1
'''

def main():
    print("t\n")
    infile = open("gift1.in", "r")
    outfile = open("gift1.out", "w")
    NP = int(infile.readline())
    names = []
    accounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(NP):
        # alternatively, use map function | t = map(lambda s : s.split(), t)
        names.append(infile.readline().strip())
    for i in range(NP):
        giver = names.index(infile.readline().strip())
        transaction = list(map(int, infile.readline().split()))
        if 0 == transaction[1]:
            continue
        accounts[giver] -= (transaction[0]-(transaction[0]%transaction[1]))
        for j in range(transaction[1]):
            reciever = names.index(infile.readline().strip())
            accounts[reciever] += int(transaction[0]/transaction[1])
    for i in range(NP):
        outfile.write(names[i] + " " + str(int(accounts[i])) + "\n")
    infile.close()
    outfile.close()
main()

