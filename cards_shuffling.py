def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
            line = [int(x) for x in data.read().split()] # Reads all data at once.

            ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
            suits = ['C','D','H','S']
            cards = [x+y for x in suits for y in ranks]

            for i in range(len(cards)):
                cards[i],cards[line[i]%52] = cards[line[i]%52],cards[i]

            for x in cards:
                print(x,end=' ')
