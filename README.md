# Turing Machine Compilator


## Syntax of compilator

```
# You can write your comment here

# At the beginning you must write initializations:
ALPHABET = {X_1, ... ,X_N}; # X_1, ... ,X_N - are symbols of TM Alphabet
EMPTY = {X_i};              # X_i - is empty symbol of ALPHABET
START_STATE = {q1};         # q1 - is initial state of TM
STOP_STATE = {q0};          # q0 - is last (halt) state of TM

# After initializations, you can wrote TM code commands:
qi,X_i -> qj,X_j,R;         # The syntax is: CURRENT_STATE,CURRENT_SYMBOL -> NEXT_STAGE,ACTION,MOVE;
```

[Here you can find an examples of code in this syntax.](src/examples/README.md)