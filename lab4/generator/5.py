def generator(N):
    for i in range(N,-1,-1):
        yield i   

N = int(input())
gener = generator(N)
for i in gener:
    print(i,end=' ')