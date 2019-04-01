import math
from math import cos as C, pi as P

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        # Distance travelled vertically for B,C,E,F
        a = C(P/6)
        p = (0,0)
        move_dict = {'A':(1,0),'B':(0.5,a),'C':(-0.5,a),\
                     'D':(-1,0),'E':(-0.5,-a),'F':(0.5,-a)}

        for line in data:
            moves = list(line.rstrip())
            move_values = [0]*len(moves)
            for i in range(len(moves)):
                move_values[i] = move_dict[moves[i]]
            p = tuple(sum(v) for v in zip(*move_values))
            print(round(math.sqrt(p[0]**2 + p[1]**2),7))
