def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            line = [x for x in line.split()]
            cards = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, \
                     'T':10, 'J': 10, 'Q':10, 'K':10, 'A':{1,11}}

            sum = 0
            aces = 0
            for x in line:
                if x == 'A':
                    aces += 1
                else:
                    sum += cards[x]

            for a in range(aces):
                if sum <= 11:
                    sum += max(cards['A'])
                else:
                    sum += min(cards['A'])

            print(sum) if sum <= 21 else print("Bust")
