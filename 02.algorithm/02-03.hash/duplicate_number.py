arr = ["a","b","c","d","e","f","c"]

def duplicate_number(arr):
    check = {}
    for m in arr:
        if not check.get(m):
            check[m] = True
        else:
            return m


print(duplicate_number(arr))