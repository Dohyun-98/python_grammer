def max(array):
    print('recursion')
    if len(array) == 1 :
        return array[0]
    
    tmp = max(array[1:])
    if array[0] > tmp:
        return array[0]
    else :
        return tmp

print(max([1,2,3,4]))