arr = [2,4,6,8,10,12,13]

def binary_search(arr, target):
    l = 0
    r = len(arr) - 1
    while l <= r :
        mid = (l + r) // 2 
        if target == arr[mid]:
            print(f'find {arr[mid]}')
            break
        
        if mid > arr[mid]:
            l = mid + 1
        else :
            r = mid - 1

num = int(input())
binary_search(arr,num)