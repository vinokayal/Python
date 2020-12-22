def Compute_Square(num):
    if num==0:
        return 0
    else:
        return Compute_Square(num-1)+(2*num)-1


num=5
print(Compute_Square(num))
