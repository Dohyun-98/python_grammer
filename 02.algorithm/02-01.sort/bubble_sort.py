def bubble_sort(list):
    # 정렬되지 않은 가장 오른쪽 인덱스
    unsorted_until_index = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
                sorted = False
                print(list[i],list[i+1])
        unsorted_until_index -= 1
    

    return list

print(bubble_sort([65,55,45,35,26,14,10]))