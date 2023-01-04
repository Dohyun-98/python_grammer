def make_inventory(clothing_items):
    clothing_options = list()
    for item in clothing_items:
        # 1부터 5까지의 각 사이즈에 대해 수행
        # 파이썬 range 두번째 인수값까지 증가하나 포함하지 않는다.
        for size in range(1,6):
            clothing_options.append(item + "Size" + str(size))


    return clothing_options

# 안쪽 반복문은 항상 5번 돌게 된다.
# O(N) + 5N이 된다.
# O(N) 이다.