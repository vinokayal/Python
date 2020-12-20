def fibonaci_series(n):
    if n<=1:
        return n
    return (fibonaci_series(n-1)+fibonaci_series(n-2))

print(fibonaci_series(7))