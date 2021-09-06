totalIncome = int(input("Enter your Income: "))

def taxCalc(totalIncome):
    totalTax = 0

    if totalIncome < 10000 and totalIncome > 0:
        totalTax = 0
    elif totalIncome > 10000 and totalIncome < 20000:
        totalTax = (totalIncome - 10000) * 10/100
    else:
        totalTax = ((totalIncome - 20000) * 20/100) + (10000 * 10/100)
    

    print("Total Payable tax is ", totalTax)
# in  print statement totalTax can be changed to int(totalTax) to get result in integers

taxCalc(totalIncome)
