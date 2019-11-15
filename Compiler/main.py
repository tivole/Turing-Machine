"""
    (c) Tivole

    Compiler for 'Turing Code'

"""

code = open('turing_code.txt', 'r')

lines = code.readlines()

while '\n' in lines:
    lines.remove('\n')

# Reading Alphabet
ALPHABET = lines[0][lines[0].find('{') + 1:lines[0].find('}')].replace(' ', '').split(',')
EMPTY = lines[1][lines[1].find('{') + 1:lines[1].find('}')].replace(' ', '').split(',')[0]

# Reading codes
CODE = []
for i in range(1, len(lines)):
    CODE.append(tuple(lines[i][:lines[i].find(';')].replace(' ', '').replace('->', ',').split(',')))


def Turing_Machine(Sequence):
    pass
