# Turing Machine Compilator

## Introdution

<b>Turing Machine</b> (TM) - an abstract performer (abstract computing machine). It was proposed by <i>Alan Turing</i> in 1936 to formalize the concept of an algorithm.

The Turing Machine is an extension of the finite state machine and, according to the Church-Turing thesis, is able to simulate all performers (by setting transition rules) that somehow implement the process of stepwise calculation in which each step of the calculation is quite elementary.

That is, any intuitive algorithm can be implemented using some Turing machine.

<p align="center">
  <img src="img/TurigMachine.png">
</p>

A turing machine consists of a tape of infinite length on which read and writes operation can be performed. The tape consists of infinite cells on which each cell either contains input symbol or
a special symbol called blank. It also consists of a head pointer which points to cell currently being read and it can move in both directions. A TM is expressed as a 7-tuple (<b>Q</b>, <b>T</b>, <b>B</b>, <b>∑</b>, <b>δ</b>, <b>q0</b>, <b>F</b>) where:

* <b>Q</b> is a finite set of states
* <b>T</b> is the tape alphabet (symbols which can be written on Tape)
* <b>B</b> is blank symbol (every cell is filled with B except input alphabet initially)
* <b>∑</b> is the input alphabet (symbols which are part of input alphabet)
* <b>δ</b> is a transition function which maps Q × T → Q × T × {L,R}. Depending on its present state and present tape alphabet (pointed by head pointer), it will move to new state, change the tape symbol (may or may not) and move head pointer to either left or right.
* <b>q1</b> is the initial state
* <b>F</b> is the set of final states. If any state of F is reached, input string is accepted.


## Syntax of compilator

```
# You can write your comment here

# At the beginning you must write initializations:
ALPHABET = {X_1, ... ,X_N}; # X_1, ... ,X_N - are symbols of TM Alphabet
EMPTY = {X_i};              # X_i - is empty (blank) symbol of ALPHABET
START_STATE = {q1};         # q1 - is initial state of TM
STOP_STATE = {q0};          # q0 - is last (halt) state of TM

# After initializations, you can wrote TM code commands:
qi,X_i -> qj,X_j,R;         # The syntax is: CURRENT_STATE,CURRENT_SYMBOL -> NEXT_STAGE,ACTION,MOVE;
```

[Here you can find an examples of code in this syntax.](src/examples/README.md)

## Visualisator

<b>Here is an example of visualisation for Turing Machine, which checks balancing bracket sequence:</b>

<p align="center">
  <img src="src/examples/Bracket%20Sequence/img/Bracket_Sequence.gif">
</p>


[Here you can find more visualisations of different turing machines.](src/examples/README.md)

## Installation of Turing_Machine

<i>Make sure you have installed [Python 3](https://www.python.org/).</i>

<b>Clone repository:</b>
* Run `git clone https://github.com/tivole/Turing_Machine.git` to clone repository.
* Run `cd Turing_Machine/src` to change directory.

<b>Install requirements:</b>
* Run `pip install -r requirements.txt` to install required libraries.

Now you can use Turing_Machine.


## Usage of Compilator and Visualisator

1. Write your TM code in `turing_code.txt`
2. Write your INPUT sequnce in `input.txt`
3. Run in terminal: `python3 main.py`


## References

1. [Turing's paper](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/plms/s2-42.1.230)
2. [The Church-Turing Thesis](https://plato.stanford.edu/entries/church-turing/)