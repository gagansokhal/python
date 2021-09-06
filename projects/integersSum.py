# Sum of a range of Integers 

num = int(input("Enter a Number: "))

def add_it_up(num):
    sum = 0

    if num > 0 :
        for i in range(0,num+1):
            sum = sum + i
        print("The sum of integers upto n is ", sum)
    else:
        print("Please enter a positive integer")

add_it_up(num)
