"""
Alan:
R1 30% chance of hitting
R2 30*50*70% chance of hitting, given that Alan missed and Bob missed
R3 30*50*70*50*70% chance of hitting, given that both missed in R2
R4 30*50*50%
...



50 + 50 50 + 50 50 50 + 50 50 50 50

50 25 12.5

50 + 

---

ends in one round:

30%

ends in >1 round:

70*50% * x

x = 30 + 70*50*x
x(1-70*50%) = 30

x = 30/65
"""

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            a,b = [int(x)/100 for x in line.split()]
            answer = a/(1-(1-a)*(1-b))
            print(round(100*answer))
