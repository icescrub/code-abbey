def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            line = [int(x) for x in line.split()]
            suitL = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
            rankL = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
            for x in line:
                suit = suitL[x//13]
                rank = rankL[x%13]
                print("{}-of-{} ".format(rank,suit))
