def find_max_number(array):
    array.sort()
    return array.pop() * array.pop() * array.pop()

print(find_max_number([1,2,3,4,5]))