def selected_sort(list):
    for i in range(0,len(list)-1):
        min_idx = i
        for j in range(i+1,len(list)):
            if(list[min_idx]>list[j]):
                min_idx = j
        if min_idx != i:
            list[i],list[min_idx] = list[min_idx],list[i]
    return list 

print(selected_sort([4,2,7,1,3]))