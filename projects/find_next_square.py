import math 

def find_next_square(sq):
    #here we find the square root of the given number and store in a float value
    ori_root = math.sqrt(sq)
    
    # then we call float function is integer to check if its true or not
    if ori_root.is_integer() is True:
        ori_root=int(ori_root) #to change the float back to int
        new_root = ori_root+1  # to get the next number after the square root
        return int(math.pow(new_root,2)) # use the math function to get square of the next num and change that to int
    else:
        return -1



print(find_next_square(121))

