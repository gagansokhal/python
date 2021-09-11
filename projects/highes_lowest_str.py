def high_and_low(numbers):
    num_list = numbers.split(" ")
    num_list.sort(key=int)
    return num_list[-1] + " " + num_list[0] 
