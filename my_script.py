def factorial(n):
    fac = n
    if n == 1:
        return fac
    else:
        fac *= factorial(n-1)
        return fac
