def factorial(n):
    fac = 1
    if n == 0:
        return fac
    else:
        fac *= factorial(n-1)
        return fac
