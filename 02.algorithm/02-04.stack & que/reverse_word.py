def reverse_word(words):
    stack = []
    result = ''
    for word in words:
        stack.append(word)

    
    for word in words:
        result += stack.pop()

    return result

print(reverse_word('hello'))
