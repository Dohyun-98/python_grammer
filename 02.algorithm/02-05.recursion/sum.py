def sum(low, hight):
    if low == hight:
        return 1
    return hight + sum(low,hight-1)


print(sum(1,10))