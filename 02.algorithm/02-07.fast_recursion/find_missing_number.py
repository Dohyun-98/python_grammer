# O(N^2) 시나리오
# def find_missing_number(array):
#     for i in range(len(array)):
#         if i not in array:
#             return i
#     return 'yes'

# O(N) 시나리오
def find_missing_number(array):
    array.sort()
    for i in range(len(array)+1):
        if i != array[i]:
            return i



print(find_missing_number([5,2,4,1,0]))