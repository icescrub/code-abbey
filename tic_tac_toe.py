# Easiest way to do this that I know.
# lines = [line.strip() for line in open('C:\\Users\\Duchess\\Desktop\\Data.txt')]

import itertools
#from itertools import combinations

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            line = [int(x) for x in line.split()]

            movesP1 = line[::2]
            movesP2 = line[1::2]            
            basicWins = [[1,2,3],[4,5,6],[7,8,9],\
                         [1,4,7],[2,5,8],[3,6,9],\
                         [1,5,9],[3,5,7]] # LIST OF LISTS

            # Player 1.
            x = list(map(list,itertools.combinations(movesP1,3)))
            xs1 = [x for x in x if x[2] == movesP1[2]]
            xs2 = [x for x in x if x[2] == movesP1[3]]
            xs3 = [x for x in x if x[2] == movesP1[4]]

            # Player 2.
            y = list(map(list,itertools.combinations(movesP2,3)))
            ys1 = [y for y in y if y[2] == movesP2[2]]
            ys2 = [y for y in y if y[2] == movesP2[3]]

            if any([sorted(x) in basicWins for x in xs1]):
                print(5)
            elif any([sorted(y) in basicWins for y in ys1]):
                print(6)
            elif any([sorted(x) in basicWins for x in xs2]):
                print(7)
            elif any([sorted(y) in basicWins for y in ys2]):
                print(8)
            elif any([sorted(x) in basicWins for x in xs3]):
                print(9)
            else:
                print(0)

            """
            P = itertools.permutations
            wins = sum([list(P(x)) for x in basicWins],[])
            board = []
            player = 1
            for x in line:
                board.append(x)
                boardWins = [P(]
                if [sorted(list(P(x))) in wins:
                    print("player" + str(player%2 + 1) + "wins on turn " + player)
                player += 1

            # wins = all possible winning moves.
            P = itertools.permutations
            basicWins = [(1,2,3),(4,5,6),(7,8,9),\
                       (1,4,7),(2,5,8),(3,6,9),\
                       (1,5,9),(3,5,7)] # LIST OF TUPLES
            
            
            movesP1 = line[::2]
            movesP2 = line[1::2]
            possibleP1 = list(P(movesP1,3)) # LIST OF TUPLES
            possibleP2 = list(P(movesP2,3)) # LIST OF TUPLES
            
            w1 = set(possibleP1)&set(wins)
            w2 = set(possibleP2)&set(wins)
            print(w1,w2)
            #y = list(filter(lambda x: x in winners, possibleWins))
            #print(y)
            #print(possibleP1.index(y) or possibleP2.index(y))
"""
