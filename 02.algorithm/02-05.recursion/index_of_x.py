def index_of_x(string):
    if string[0] == 'x':
        return 1
    return 1 + index_of_x(string[1:])

print(index_of_x('abcdefgx'))