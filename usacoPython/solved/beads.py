# NAME                         :   Lucas Oeming
# GROUP                        :   APCS
# LAST MODIFIED                :   09/30/2022
# PROBLEM ID                   :   USACO Broken Necklace
# DESCRIPTION                  :   Usaco beads problem, optimized
# SOURCES/HELPERS              :   Usaco, stackoverflow
# PEOPLE I HELPED              :   N/A
# PEOPLE WHO HELPED ME         :   N/A

'''
ID: basscla2
LANG: PYTHON3 
TASK: beads
'''

from re import finditer
# open file to read
infile = open("beads.in", "r")
# create string with 2 copies of input removing all delimiters
string = (infile.readlines()[1] * 2).replace(' ', '').replace('\n', '')
# use finditer to match all regexes to string, and pick the maximum length match considering breaks with 'rb' or 'br' center, use 0 as default case if none found
top = max([len(match.group(1)) for match in finditer(r'(?=([^r]+[^b]+))',string)] + [len(match.group(1)) for match in finditer(r'(?=([^b]+[^r]+))',string)] + [0])
# output max length to file, considering edge cases such as single color strings or matches longer than input string
open("beads.out", "w").write(str(int(len(string)/2)) + "\n") if top > (len(string)/2) or top == 0 else open("beads.out", "w").write(str(top) + "\n")

 