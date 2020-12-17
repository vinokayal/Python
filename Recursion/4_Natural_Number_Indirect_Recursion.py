def NaturalNumbers(lowerRange,upperRange):
    if lowerRange <= upperRange:
        print(lowerRange)
        lowerRange += 1
        helperFunction(lowerRange,upperRange)
    else:
        return

def helperFunction(lowerRange,upperRange):
    if lowerRange<=upperRange:
        print(lowerRange)
        lowerRange += 1
        NaturalNumbers(lowerRange,upperRange)
    else:
        return



n=5
NaturalNumbers(1,5)