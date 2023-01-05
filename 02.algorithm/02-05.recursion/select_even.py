def select_even(array):
    if(len(array)==0):
        return []
    if array[0] % 2 == 0:
        return [array[0]] + select_even(array[1:len(array)])
    else:
        return select_even(array[1:len(array)])

print(select_even([0,1,2,3,4,5,6]))