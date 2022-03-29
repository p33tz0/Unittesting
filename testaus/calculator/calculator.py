# function that returns sum of two numbers
def plus(x, y):
    g = float("{0:.2f}".format(x + y))
    return g


# function that returns difference of two numbers
def minus(x, y):
    g = float("{0:.2f}".format(x - y))
    return g


# function that returns quotient of two numbers
def jako(x, y):
    # Raise error if dividing zero or dividing by zero
    if y == 0 or x == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero")
    else:    
        g = float("{0:.2f}".format(x / y))
        return g




# function that returns product of two numbers
def kertolasku(x, y):
    g = float("{0:.2f}".format(x * y))
    return g


# function that returns power of two numbers
def potenssi(x, y):
    g = float("{0:.2f}".format(x**y))
    return g
