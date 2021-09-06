#function to return base to power to exponent

baseInt = int(input("Enter the base integer: "))
expInt = int(input("Enter the exponent: "))

def exponent(base,exp):
    finalValue = 0
    if exp >= 0 :
        finalValue = baseInt ** expInt
        print(baseInt," raised to the power of ",expInt," is ",finalValue)

    else:
        print("Exponent Must be a non negative integer")


exponent(baseInt,expInt)
