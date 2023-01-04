def double_array(array,index):
    if index == len(array):
        return
    array[index] *= 2
    double_array(array,index+1)
