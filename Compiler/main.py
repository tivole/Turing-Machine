import compiler

input_s = open('input.txt', 'r')

Sequence = input_s.readline()

Sequences_OUTPUT = compiler.Turing_Machine(Sequence)