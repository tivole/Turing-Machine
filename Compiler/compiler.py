"""
    (c) Tivole

    Compiler for 'Turing Code'

"""

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
for __i__ in range(1, len(__lines__)):
    __CODE__.append(tuple(__lines__[__i__][:__lines__[__i__].find(';')].replace(' ', '').replace('->', ',').split(',')))


def Turing_Machine(Sequence):
    """
        Function to program Turing Machine code.
    """
    Sequence = __EMPTY__ * __NUMBER_OF_EMPTY__ + Sequence + __EMPTY__ * __NUMBER_OF_EMPTY__
    
    return Sequence
