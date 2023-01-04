# 시간 복잡도 O(N)

array1 = [1,2,3,4,5]
array2 = [0,2,4,6,8]

def exist_number(arr1,arr2):
    search_arr = {}
    result = []
    for a1 in arr1:
        search_arr[a1] = True
    
    for a2 in arr2:
        if search_arr.get(a2) == True:
            result.append(a2)

    return result
print(exist_number(array1,array2))