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

while '\n' in __lines__:
    __lines__.remove('\n')

# Reading Alphabet
__ALPHABET__ = __lines__[0][__lines__[0].find('{') + 1:__lines__[0].find('}')].replace(' ', '').split(',')
__EMPTY__ = __lines__[1][__lines__[1].find('{') + 1:__lines__[1].find('}')].replace(' ', '').split(',')[0]
__NUMBER_OF_EMPTY__ = int(__lines__[1][__lines__[1].find('{') + 1:__lines__[1].find('}')].replace(' ', '').split(',')[1])

# Reading codes
__CODE__ = []
for __i__ in range(2, len(__lines__)):
    __CODE__.append(tuple(__lines__[__i__][:__lines__[__i__].find(';')].replace(' ', '').replace('->', ',').split(',')))


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
