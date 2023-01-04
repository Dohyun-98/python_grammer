string = '{([])}'

def is_not_error(string):
    stack = []
    for s in string:
        if s == '{' or s == '[' or s == '(':
            stack.append(s)
        elif s =='}' or s ==']' or s == ')':
            v = stack.pop()
            if ( s == '}' and not v == '{'):
                return False
            elif ( s == ']' and not v == '['):
                return False
            elif (s == ')' and  not v == '('):
                return False


    if len(stack) != 0:
        return False
    
    return True


print(is_not_error(string))
print(is_not_error('{)'))
