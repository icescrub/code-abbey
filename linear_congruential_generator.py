def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            A,C,M,X,N = list(int(x) for x in line.split())
          # A, C, M, x0, N = map(int, input().split())
            
            for i in range(N):
                global X
                X = (A*X + C)%M
            print(X)
