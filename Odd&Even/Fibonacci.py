firstNumber = int(input("Enter number the first number "))
lastNumber = int(input("Enter number till how much you want the fibonacci series "))
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2)+fibonacci(n-1)
print map(fibonacci, xrange(firstNumber,lastNumber))