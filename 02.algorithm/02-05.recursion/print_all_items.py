def print_all_items(array):
    for value in array:
        if isinstance(value,list):
            print_all_items(value)
        else :
            print(value)