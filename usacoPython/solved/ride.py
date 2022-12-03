'''
ID: basscla2
LANG: PYTHON3
TASK: ride
'''

from math import prod 

def main():

    # one line bb
    open("ride.out", "w").write(("GO\n" if prod([ord(i)-64 for i in open("ride.in").readlines()[0][0:-1]]) % 47 == prod([ord(i)-64 for i in open("ride.in").readlines()[1][0:-1]]) % 47 else "STAY\n"))
main()

