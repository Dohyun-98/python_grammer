def missing_letter(string):
    check = {}
    string.replace(' ','')
    for x in string:
        check[x] = True
    
    find_string = 'abcdefghijklmnopqrstuvwxyz'
    for x in find_string:
        if not check.get(x):
            return x

print(missing_letter('the quick brown box jumps over a lazy dog'))