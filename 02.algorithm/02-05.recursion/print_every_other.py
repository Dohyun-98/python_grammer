def print_every_other(low,hight):
    if low > hight:
        return 
    print(low)
    print_every_other(low+2,hight)


print(print_every_other(0,10))