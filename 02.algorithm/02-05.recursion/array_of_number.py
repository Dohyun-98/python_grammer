def array_of_number(array):
    if(len(array)==0):
        return 0
    return len(array[0]) + array_of_number(array[1:len(array)])

print(array_of_number(["asd","asdas","sv"]))