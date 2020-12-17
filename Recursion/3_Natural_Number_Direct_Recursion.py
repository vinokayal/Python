def printNaturalNumbers(lowerRange, upperRange):
    # Base Case
    if lowerRange > upperRange:
        return

    print(lowerRange)

    # Recursive Case
    printNaturalNumbers(lowerRange + 1, upperRange);


# Driver Code
n = 5
printNaturalNumbers(1, n)