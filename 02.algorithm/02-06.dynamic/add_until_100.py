# def add_until_100(array):
#     if len(array) == 0:
#         return 0
#     if array[0] + add_until_100(array[1:]) > 1000 :
#         return add_until_100( array[1:])
#     else:
#         return array[0] + add_until_100(array[1:])
    

def add_until_100(array):
    if len(array) == 0:
        return 0
    tmp = add_until_100(array[1:])
    if array[0] + tmp > 1000 :
        return tmp
    else:
        return array[0] + tmp
    