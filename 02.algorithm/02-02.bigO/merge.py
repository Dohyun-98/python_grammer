# 시간복잡도 :  O(N+M)
def merge(arr1, arr2):
    new_arr = list()
    arr1_pointer = 0
    arr2_pointer = 0

    while  arr1_pointer < len(arr1) or arr2_pointer < len(arr2):
        # 두배열이 모두 끝에 도달할 때 까지

        # 첫번째 배열이 끝에 도달할 경우 두번째 배열의 항목을 추가
        if not arr1[arr1_pointer]:
            new_arr.append(arr2[arr2_pointer])
            arr2_pointer += 1
        
        elif not arr2[arr2_pointer]:
            new_arr.append(arr1[arr1_pointer])
            arr1_pointer += 1

        elif arr1[arr1_pointer] < arr2_pointer[arr2_pointer]:
            new_arr.append(arr1[arr1_pointer])
            arr1_pointer += 1
        else :
             new_arr.append(arr2[arr2_pointer])
             arr2_pointer += 1
    
    return new_arr