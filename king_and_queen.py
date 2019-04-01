def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
            for line in data:
                K,Q = [str(x) for x in line.split()]
                Kf,Kr = ord(K[0]) - 96,int(K[1])
                Qf,Qr = ord(Q[0]) - 96,int(Q[1])
                print('Y') if [Kf,Kr] in purview([Qf,Qr]) else print('N')

def purview(Q):
    Qf = Q[0]
    Qr = Q[1]
    threats = []
    for i in range(1,9):
        threats.append([Qf,i]) # holds f constant, so horizontal purview
        threats.append([i,Qr]) #holds f constant, so vertical purview
    for i in range(1,8):
        threats.append([Qf-i,Qr-i]) # all diag DL
        threats.append([Qf-i,Qr+i]) # all diag UL
        threats.append([Qf+i,Qr+i]) # all diag UR
        threats.append([Qf+i,Qr-i]) # all diag DR
    return threats
