def triangular_numbers(num):
    if num == 0:
        return 0
    return num + triangular_numbers(num-1)

print(triangular_numbers(7))