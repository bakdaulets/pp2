def squaregen(ab):
    for i in range(ab[0],ab[1]+1):
        yield (i**2)   

ab = [int(i) for i in input().split()]
sq = squaregen(ab)
for square in sq:
    print(square,end = ' ')