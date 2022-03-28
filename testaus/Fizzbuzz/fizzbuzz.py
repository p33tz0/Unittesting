#Function that returns Fizz if number is divided by 3
def fizz(x):
    if x % 3 == 0:
        return "Fizz"
    else:
        return x

def buzz(x):
    if x % 5 == 0:
        return "Buzz"
    else:
        return x

def fizzbuzz(x):
    if x % 15 == 0:
        return "FizzBuzz"
    else:
        return x
    
#Function that takes a number and returns Fizz, Buzz or FizzBuzz
def num(x):
    if x % 3 == 0 and x % 5 == 0:
        return fizzbuzz(x)
    elif x % 3 == 0:
        return fizz(x)
    elif x % 5 == 0:
        return buzz(x)
    else:
        return x