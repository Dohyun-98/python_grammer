def average_celsius(array):
    celsius_numbers = list()

    for number in array:
        celsius_conversion = (number - 32) /1.8
        celsius_numbers.append(celsius_conversion)  
    sum = 0
    for celsius_number in celsius_numbers:
        sum += celsius_number

    return sum / len(celsius_numbers)