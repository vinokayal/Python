def gcd(num1, num2):
    #Base Case
    if num1 == num2:
        return num1
    #Recursive Case
    if num1 > num2:
        return gcd(num1-num2, num2)
    else:
        return gcd(num1,num2-num1)

num1=6
num2=9
print(gcd(num1,num2))
