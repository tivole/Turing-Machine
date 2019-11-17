"""
    (c) Tivole

    Compiler for 'Turing Code'

"""

# Libraries
import copy

__code__ = open('turing_code.txt', 'r')

__lines__ = __code__.readlines()
__lines_backend__ = copy.deepcopy(__lines__)

# Removing empty lines
while '\n' in __lines__:
    __lines__.remove('\n')

# Checking for symbols ';', ',', '->', '{' and '}'
__passed_lines__ = 0
__checked_codes__ = []
for __i__ in range(len(__lines__)):
    __passed_lines__ += 1
    if '#' in __lines__[__i__]:
        __checking_line__ = __lines__[__i__][:__lines__[__i__].find('#')]
        if __checking_line__ == '':
            __passed_lines__ -= 1
            continue
    else:
        __checking_line__ = __lines__[__i__]

    # Check for symbol ';'
    assert ';' in __checking_line__, f'(!) Compilation Error. Missing \';\' in line {__lines_backend__.index(__lines__[__i__]) + 1}'
    
    if __passed_lines__ >= 5:
        # Check for symbol '->'
        assert '->' in __checking_line__, f'(!) Compilation Error. Missing \'->\' in line {__lines_backend__.index(__lines__[__i__]) + 1}'
        
        # Check for symbol ','
        assert __checking_line__.count(',') == 3, f'(!) Compilation Error. Invalid syntax in line {__lines_backend__.index(__lines__[__i__]) + 1}'

        # Check for unkown commands
        __unknown_command__ = __checking_line__[__checking_line__.find(';') + 1:].replace('\n', '')
        assert __checking_line__[__checking_line__.find(';') + 1:].replace(' ', '').replace('\n', '') in '', f'(!) Compilation Error. Unkown command \'{__unknown_command__}\' in line {__lines_backend__.index(__lines__[__i__]) + 1}'
    
        # Check for double commands
        assert not __checking_line__.replace('\n', '') in __checked_codes__, f'(!) Compilation Error. Doubled Turing code in line {__lines_backend__.index(__lines__[__i__]) + 1}'
        __checked_codes__.append(__checking_line__.replace('\n', ''))
    else:
        assert '{' in __checking_line__, '(!) Compilation Error. Missing \'{\'' + f' in line {__lines_backend__.index(__lines__[__i__]) + 1}'
        assert '}' in __checking_line__, '(!) Compilation Error. Missing \'}\'' + f' in line {__lines_backend__.index(__lines__[__i__]) + 1}'


# Removing commentaries for compiling
for __i__ in range(len(__lines__)):
    if '#' in __lines__[__i__]:
        if __lines__[__i__].find('#') > 0:
            __lines__[__i__] = __lines__[__i__][:__lines__[__i__].find('#')]
        else:
            __lines__[__i__] = '\n'


# Removing unnecessary symbols for compiling
for __i__ in range(len(__lines__)):
    # Removing ' '
    if ' ' in __lines__[__i__]:
        __lines__[__i__] = __lines__[__i__].replace(' ', '')

    # Removing '\n'
    if '\n' in __lines__[__i__]:
        __lines__[__i__] = __lines__[__i__].replace('\n', '')


# Removing empty lines
while '' in __lines__:
    __lines__.remove('')


# Checking Alphabet
assert 'ALPHABET' in __lines__[0], '(!) Compilation Error. ALPHABET is missing!'

# Checking Empty symbol
assert 'EMPTY' in __lines__[1], '(!) Compilation Error. Empty symbol (\'EMPTY\') is missing!'

# Checking START_STATE and STOP_STATE 
assert 'START_STATE' in __lines__[2], '(!) Compilation Error. START_STATE is missing!'
assert 'STOP_STATE' in __lines__[3], '(!) Compilation Error. STOP_STATE is missing!'

# Reading Alphabet
__ALPHABET__ = __lines__[0][__lines__[0].find('{') + 1:__lines__[0].find('}')].replace(' ', '').split(',')

# Reading Empty symbol
__EMPTY__ = __lines__[1][__lines__[1].find('{') + 1:__lines__[1].find('}')].replace(' ', '').split(',')[0]
__NUMBER_OF_EMPTY__ = int(__lines__[1][__lines__[1].find('{') + 1:__lines__[1].find('}')].replace(' ', '').split(',')[1])

# Readding START_STATE and STOP_STATE
__START_STATE__ = __lines__[2][__lines__[2].find('{') + 1:__lines__[2].find('}')].replace(' ', '')
__STOP_STATE__ = __lines__[3][__lines__[3].find('{') + 1:__lines__[3].find('}')].replace(' ', '')

# Checking EMPTY symbol
assert __EMPTY__ in __ALPHABET__, f'(!) Compilation Error. Empty symbol \'{__EMPTY__}\' is not found in ALPHABET.'

# Reading codes
__CODE__ = []
for __i__ in range(4, len(__lines__)):
    __CODE__.append(tuple(__lines__[__i__][:__lines__[__i__].find(';')].replace(' ', '').replace('->', ',').split(',')))


# Checking is all symbols from ALPHABET
for __i__ in range(len(__CODE__)):
    assert __CODE__[__i__][1] in __ALPHABET__, f'(!) Compilation Error. Symbol \'{__CODE__[__i__][1]}\' not found in the ALPHABET.'
    assert __CODE__[__i__][3] in __ALPHABET__, f'(!) Compilation Error. Symbol \'{__CODE__[__i__][3]}\' not found in the ALPHABET.'
    assert __CODE__[__i__][4] in ['L', 'R', 'S'], f'(!) Compilation Error. Symbol \'{__CODE__[__i__][4]}\' is unknown. Use only L, R or S.'

# Checking is all states defined
for __i__ in range(len(__CODE__)):
    if __CODE__[__i__][2] != __STOP_STATE__:
        assert __CODE__[__i__][2] in [__CODE__[__j__][0] for __j__ in range(len(__CODE__))], f'(!) Compilation Error. Udefined state \'{__CODE__[__i__][2]}\''

# Checking is __START_STATE__ defined
assert __START_STATE__ in [__CODE__[__j__][0] for __j__ in range(len(__CODE__))], f'(!) Compilation Error. Start state \'{__START_STATE__}\' is undefined.'


def get_empty_symbol():
    return __EMPTY__


def Turing_Machine(Sequence_INPUT):
    """
        Function to program Turing Machine code.
    """

    # Checking INPUT Sequence
    for c in Sequence_INPUT:
        assert c in __ALPHABET__, f'(!) Compilation Error. Unknown symbol \'{c}\' in input data. Check ALPHABET.'

    Sequence_INPUT = list(__EMPTY__ * __NUMBER_OF_EMPTY__ + Sequence_INPUT + __EMPTY__ * __NUMBER_OF_EMPTY__)
    Sequence = copy.deepcopy(Sequence_INPUT)
    
    state = __START_STATE__

    # Put the machine_arrow in the right place
    machine_arrow = 0
    while Sequence_INPUT[machine_arrow] == __EMPTY__:
        machine_arrow += 1

    Sequences_OUTPUT = []

    Sequences_OUTPUT.append([copy.deepcopy(Sequence_INPUT), state, machine_arrow, ''])

    TM_STOP = False

    while not TM_STOP:
        Find = False
        for i in range(len(__CODE__)):
            STOP = False
            if state == __CODE__[i][0] and Sequence[machine_arrow] == __CODE__[i][1]:
                Find = True
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

        if not Find:
            assert Find, f'(!) Compilation Error. Undefined action for state=\'{state}\' and symbol \'{Sequence[machine_arrow]}\'.'
            break

        Sequences_OUTPUT.append([copy.deepcopy(Sequence), state, machine_arrow, __CODE__[i][4]])

        if state == __STOP_STATE__ and STOP == True:
            TM_STOP = True


    return Sequences_OUTPUT
