def even_odd(a,b):
    for i in range(a,b):
        if i%2==0:
            print(f'{i} is even number')
        else:
            print(f"{i} is odd number")
    #return a,b
even_odd(1,10)