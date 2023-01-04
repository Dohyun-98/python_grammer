# 시간 복잡도 : O(N) / 2 
def one_hundred_sum(array):
    left = 0
    right = len(array) -1

    while left < len(array) // 2:
        if array[left] + array[right] != 100:
            return False
        left += 1
        right -= 1

    
    return True
