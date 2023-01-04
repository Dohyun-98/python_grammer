string = 'minimum'

def first_none_duplicate(string):
    check = {}
    for x in string:
        if not check.get(x):
            check[x] = 1
        else :
            check[x] = check.get(x)+1

    for x in string:
        if check.get(x) == 1:
            return x

    return -1

print(first_none_duplicate(string))