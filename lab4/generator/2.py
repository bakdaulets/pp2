def even_generator(N):
    for i in range(0,N):
        if(i%2==0):
            yield i
          
N=int(input())
even_gen = even_generator(N)

for i in even_gen:
    print(i,end = ', ')