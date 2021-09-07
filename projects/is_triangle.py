def is_triangle(a, b, c):
        # sum of two sides is always greater than 3rd side
    if (a+b > c and a+c > b and b+c >a) :
        return True
    else:
        return False
   
