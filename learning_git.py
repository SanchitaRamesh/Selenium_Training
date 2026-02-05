class Numbers:
    def even_odd(self,a,b):
        for i in range(a,b):
            if i%2==0:
                print(f'{i} is even number')
            else:
                print(f"{i} is odd number")
        #return a,b
num = Numbers()
num.even_odd(1,10)
#even_odd(1,10)