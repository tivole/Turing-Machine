import pygame
import time
import copy

f = open('input.txt', 'r')

Sequence = f.readline()

f.close()

Sequence = 'A' + Sequence + 'A'
Sequence = list(Sequence)

state = 'q1'
machine_arrow = 1
halt = False
t = 0
go = ''

Sequence_t = []
Sequence_t.append([copy.deepcopy(Sequence), state, machine_arrow, go])

while True:

    if state == 'q1' and Sequence[machine_arrow] == '(':
        Sequence[machine_arrow] = '('
        machine_arrow += 1 # go RIGHT
        go = 'R'
        state = 'q1'
    
    elif state == 'q1' and Sequence[machine_arrow] == ')':
        Sequence[machine_arrow] = 'X'
        machine_arrow -= 1 # go LEFT
        go = 'L'
        state = 'q2'

    elif state == 'q1' and Sequence[machine_arrow] == 'X':
        Sequence[machine_arrow] = 'X'
        machine_arrow += 1 # go RIGHT
        go = 'R'
        state = 'q1'

    elif state == 'q1' and Sequence[machine_arrow] == 'A':
        Sequence[machine_arrow] = 'A'
        machine_arrow -= 1 # go LEFT
        go = 'L'
        state = 'q3'

    elif state == 'q2' and Sequence[machine_arrow] == '(':
        Sequence[machine_arrow] = 'X'
        machine_arrow += 1 # go RIGHT
        go = 'R'
        state = 'q1'

    elif state == 'q2' and Sequence[machine_arrow] == ')':
        Sequence[machine_arrow] = ')'
        machine_arrow -= 1 # go LEFT
        go = 'L'
        state = 'q2'

    elif state == 'q2' and Sequence[machine_arrow] == 'X':
        Sequence[machine_arrow] = 'X'
        machine_arrow -= 1 # go LEFT
        go = 'L'
        state = 'q2'

    elif state == 'q2' and Sequence[machine_arrow] == 'A':
        Sequence[machine_arrow] = 'A'
        machine_arrow += 1 # go RIGHT
        go = 'R'
        state = 'q4'

    elif state == 'q3' and Sequence[machine_arrow] == '(':
        Sequence[machine_arrow] = '0'
        machine_arrow = machine_arrow # HALT
        go = 'S'
        halt = True
        state = 'q0'

    elif state == 'q3' and Sequence[machine_arrow] == ')':
        # IMPOSSIBLE
        pass

    elif state == 'q3' and Sequence[machine_arrow] == 'X':
        Sequence[machine_arrow] = 'A'
        machine_arrow -= 1 # go LEFT
        go = 'L'
        state = 'q3'

    elif state == 'q3' and Sequence[machine_arrow] == 'A':
        Sequence[machine_arrow] = '1'
        machine_arrow = machine_arrow # HALT
        go = 'S'
        halt = True
        state = 'q0'

    elif state == 'q4' and Sequence[machine_arrow] == '(':
        Sequence[machine_arrow] = 'A'
        machine_arrow -= 1 # go LEFT
        go = 'L'
        state = 'q4'

    elif state == 'q4' and Sequence[machine_arrow] == ')':
        # IMPOSSIBLE
        pass

    elif state == 'q4' and Sequence[machine_arrow] == 'X':
        Sequence[machine_arrow] = 'A'
        machine_arrow -= 1 # go LEFT
        go = 'L'
        state = 'q4'

    elif state == 'q4' and Sequence[machine_arrow] == 'A':
        Sequence[machine_arrow] = '0'
        machine_arrow = machine_arrow # HALT
        go = 'S'
        halt = True
        state = 'q0'

    t += 1
    Sequence_t.append([copy.deepcopy(Sequence), state, machine_arrow, go])


    if state == 'q0' and halt == True:
        if Sequence[machine_arrow] == '1':
            print('YES')
        elif Sequence[machine_arrow] == '0':
            print('NO')
        break


pygame.font.init()


DELAY_TIME = 6
WIDTH = 805
HEIGHT = 500
FONT = pygame.font.SysFont("comicsans", 50)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Turing Machine')


def draw_rect(screen, color, x, y, width, height, border, symbol, text_color):
    pygame.draw.rect(win, clr, [x, y, width, height], border)
    text = FONT.render(symbol, 1, text_color)

    if text_color == (255, 255, 255) and symbol == 'A':
        text = FONT.render(symbol, 1, (150, 150, 150))

    win.blit(text, (x + 25, y + 25))


def draw_circle(screen, color, x, y, R, border, symbol):
    pygame.draw.circle(screen, color, (x, y), R, border)
    text = pygame.font.SysFont("comicsans", 30).render(symbol, 1, (255, 255, 255))
    win.blit(text, (x - 10, y - 8))



def print_command(prev, prev_st, prev_sym, st, sym, direction):
    pygame.draw.rect(win, (0, 0, 0), [260, 330, 350, 90])
    text = pygame.font.SysFont("Arial", 50).render(f'{prev_st} {prev_sym} -> {st} {sym} {direction}', 1, (255, 255, 255))
    win.blit(text, (270, 340))


def print_sequence_type(sym):
    pygame.draw.rect(win, (0, 0, 0), [260, 330, 350, 90])

    text = pygame.font.SysFont("Arial", 50).render(f'IMPOSSIBLE', 1, (0, 0, 0))

    if sym == '1':
        text = pygame.font.SysFont("Arial", 50).render(f'YES', 1, (0, 255, 0))
    elif sym == '0':
        text = pygame.font.SysFont("Arial", 50).render(f'NO', 1, (255, 0, 0))
    
    win.blit(text, (340, 340))


def print_tivole():
    # Cantarell
    # Latin Modern Mono Prop
    text_1 = pygame.font.SysFont("Cantarell", 35, bold=True).render(f'Coded by', 1, (255, 255, 255))
    text_2 = pygame.font.SysFont("Cantarell", 35, bold=True).render(f'tivole', 1, (0, 255, 45))
    win.blit(text_1, (220 + 35, 10))
    win.blit(text_2, (375 + 35, 10))


x = 5
y = 120
width = 75
height = 75
vel = 5
clr = (255, 255, 0)
border = 5
space = 5

L = 0

t = 0
run = True

left = False
right = False

prev = 1
prev_st = 'q1'
prev_sym = Sequence_t[0][0][1]

while run:
    pygame.time.delay(300)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if t != len(Sequence_t):
        win.fill((0,0,0))
        st = Sequence_t[t][1]
        ma = Sequence_t[t][2]
        x = space
        xx = []

        if ma - L > 8:
            right = True
            L += 1

        elif L > 0 and ma == L and ma < prev:
            left = True

        N = len(Sequence)

        print_tivole()

        if not left and not right:
            for i in range(N):
                x = space*(i+1) + i*width
                xx.append(x + width//2)
                sym = Sequence_t[t][0][i]
                
                if ma == i:
                    draw_rect(win, clr, x - 80*L, y, width, height, border, sym, (0, 255, 0))
                else:
                    draw_rect(win, clr, x - 80*L, y, width, height, border, sym, (255, 255, 255))

                if t != len(Sequence_t) - 1:
                    print_command(prev, prev_st, prev_sym, st, Sequence_t[t][0][ma], Sequence_t[t+1][3])
                else:
                    print_sequence_type(Sequence_t[t][0][ma])
        elif left:
            for k in range(80*L, 80*(L-1) - 1, -1):
                pygame.draw.rect(win, (0, 0, 0), [0, 115, 805, 85])
                for i in range(N):
                    x = space*(i+1) + i*width
                    xx.append(x + width//2)
                    sym = Sequence_t[t][0][i]

                    if ma == i:
                        draw_rect(win, clr, x - k, y, width, height, border, sym, (0, 255, 0))
                    else:
                        draw_rect(win, clr, x - k, y, width, height, border, sym, (255, 255, 255))
                draw_circle(win, (255, 0, 0), xx[ma] - 80*(L-1), 230, 30, 3, st)
                pygame.display.update()
                pygame.time.delay(DELAY_TIME)

                if t != len(Sequence_t) - 1:
                    print_command(prev, prev_st, prev_sym, st, Sequence_t[t][0][ma], Sequence_t[t+1][3])
                else:
                    print_sequence_type(Sequence_t[t][0][ma])
        elif right:
            for k in range(80*(L-1), 80*L + 1):
                pygame.draw.rect(win, (0, 0, 0), [0, 115, 805, 85])
                for i in range(N):
                    x = space*(i+1) + i*width
                    xx.append(x + width//2)
                    sym = Sequence_t[t][0][i]
                    
                    if ma == i:
                        draw_rect(win, clr, x - k, y, width, height, border, sym, (0, 255, 0))
                    else:
                        draw_rect(win, clr, x - k, y, width, height, border, sym, (255, 255, 255))
                draw_circle(win, (255, 0, 0), xx[ma] - 80*L, 230, 30, 3, st)
                pygame.display.update()
                pygame.time.delay(DELAY_TIME)

                if t != len(Sequence_t) - 1:
                    print_command(prev, prev_st, prev_sym, st, Sequence_t[t][0][ma], Sequence_t[t+1][3])
                else:
                    print_sequence_type(Sequence_t[t][0][ma])

        if left or right or prev == ma:
            pygame.draw.rect(win, (0, 0, 0), [0, 200, 805, 60])
            if left:
                draw_circle(win, (255, 0, 0), xx[ma] - 80*(L-1), 230, 30, 3, st)
            else:
                draw_circle(win, (255, 0, 0), xx[ma] - 80*L, 230, 30, 3, st)
            pygame.display.update()   

        elif prev < ma:
            for x_pos in range(xx[prev], xx[ma] + 1):
                pygame.draw.rect(win, (0, 0, 0), [0, 200, 805, 60])
                draw_circle(win, (255, 0, 0), x_pos - 80*L, 230, 30, 3, st)
                pygame.display.update()
                pygame.time.delay(DELAY_TIME)
        elif prev > ma:
            for x_pos in range(xx[prev], xx[ma] - 1, -1):
                pygame.draw.rect(win, (0, 0, 0), [0, 200, 805, 60])
                draw_circle(win, (255, 0, 0), x_pos - 80*L, 230, 30, 3, st)
                pygame.display.update()
                pygame.time.delay(DELAY_TIME)

        if left:
            L -= 1
        left = False
        right = False

        
        

        prev = ma
        prev_st = st
        
        if t != len(Sequence_t) - 1:
            prev_sym = Sequence_t[t+1][0][1]

        t += 1

    pygame.display.update()


pygame.quit()

