num = int(input("Enter a number: "))

def reverseDigit(num):

    while num > 0:
        digit = num % 10
        print(digit,end=" ")
        num = num // 10 
        

reverseDigit(num)
