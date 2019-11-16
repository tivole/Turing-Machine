"""
    (c) Tivole

    Compiler for 'Turing Code'

"""

"""
    TODO list:

    1) TODO: Check syntax correction.

"""

# Libraries
import copy

__code__ = open('turing_code.txt', 'r')

__lines__ = __code__.readlines()
__lines_backend__ = copy.deepcopy(__lines__)


while '\n' in __lines__:
    __lines__.remove('\n')

# Checking for sybols ';', ',' and '->'
for __i__ in range(len(__lines__)):
    assert ';' in __lines__[__i__], f'(!) Compilation Error. Missing \';\' in line {__lines_backend__.index(__lines__[__i__] + 1)}'
    if __i__ > 1:
        assert '->' in __lines__[__i__], f'(!) Compilation Error. Missing \'->\' in line {__lines_backend__.index(__lines__[__i__]) + 1}'
        assert __lines__[__i__].count(',') == 3, f'(!) Compilation Error. Invalid syntax in line {__lines_backend__.index(__lines__[__i__]) + 1}'

# Checking Alphabet
assert 'ALPHABET' in __lines__[0], '(!) Compilation Error. ALPHABET Not Found!'

# Checking Empty symbol
assert 'EMPTY' in __lines__[1], '(!) Compilation Error. Empty symbol (\'EMPTY\') Not Found!'

# Reading Alphabet
__ALPHABET__ = __lines__[0][__lines__[0].find('{') + 1:__lines__[0].find('}')].replace(' ', '').split(',')

# Reading Empty symbol
__EMPTY__ = __lines__[1][__lines__[1].find('{') + 1:__lines__[1].find('}')].replace(' ', '').split(',')[0]
__NUMBER_OF_EMPTY__ = int(__lines__[1][__lines__[1].find('{') + 1:__lines__[1].find('}')].replace(' ', '').split(',')[1])

# Reading codes
__CODE__ = []
for __i__ in range(2, len(__lines__)):
    __CODE__.append(tuple(__lines__[__i__][:__lines__[__i__].find(';')].replace(' ', '').replace('->', ',').split(',')))


# Checking is all symbols from ALPHABET
for __i__ in range(len(__CODE__)):
    assert __CODE__[__i__][1] in __ALPHABET__, f'(!) Compilation Error. Symbol \'{__CODE__[__i__][1]}\' not found in the ALPHABET.'
    assert __CODE__[__i__][3] in __ALPHABET__, f'(!) Compilation Error. Symbol \'{__CODE__[__i__][3]}\' not found in the ALPHABET.'
    assert __CODE__[__i__][4] in ['L', 'R', 'S'], f'(!) Compilation Error. Symbol \'{__CODE__[__i__][4]}\' is unknown. Use only L, R or S.'


for __i__ in range(len(__CODE__)):
    if __CODE__[__i__][2] != 'q0':
        assert __CODE__[__i__][2] in [__CODE__[__j__][0] for __j__ in range(len(__CODE__))], f'(!) Compilation Error. Udefined state \'{__CODE__[__i__][2]}\''


def Turing_Machine(Sequence_INPUT):
    """
        Function to program Turing Machine code.
    """
    Sequence_INPUT = list(__EMPTY__ * __NUMBER_OF_EMPTY__ + Sequence_INPUT + __EMPTY__ * __NUMBER_OF_EMPTY__)
    Sequence = copy.deepcopy(Sequence_INPUT)
    
    state = 'q1' # The first state must be 'q1' TODO: check in syntax

    machine_arrow = 0
    # Put the machine_arrow in the right place
    while Sequence_INPUT[machine_arrow] == __EMPTY__:
        machine_arrow += 1

    Sequences_OUTPUT = []

    Sequences_OUTPUT.append([copy.deepcopy(Sequence_INPUT), state, machine_arrow, ''])

    TM_STOP = False

    

    while not TM_STOP:
        for i in range(len(__CODE__)):
            STOP = False
            if state == __CODE__[i][0] and Sequence[machine_arrow] == __CODE__[i][1]:
                Sequence[machine_arrow] = __CODE__[i][3]
                state = __CODE__[i][2]
                if __CODE__[i][4] == 'R':
                    machine_arrow += 1 # Go RIGHT
                elif __CODE__[i][4] == 'L':
                    machine_arrow -= 1 # Go LEFT
                elif __CODE__[i][4] == 'S':
                    machine_arrow = machine_arrow  # STOP
                    STOP = True
                break

        Sequences_OUTPUT.append([copy.deepcopy(Sequence), state, machine_arrow, __CODE__[i][4]])

        if state == 'q0' and STOP == True:
            TM_STOP = True



    return Sequences_OUTPUT
