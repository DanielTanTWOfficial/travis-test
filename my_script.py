def factorial(n):
    fac = 0
    if n == 0:
        return fac
    else:
        fac *= factorial(n-1)
        return fac
