def numbers_of_paths(num):
    if num < 0 :
        return 0
    if num == 1 or num == 0:
        return 1
    
    return numbers_of_paths(num-1) + numbers_of_paths(num-2) + numbers_of_paths(num-3)
    