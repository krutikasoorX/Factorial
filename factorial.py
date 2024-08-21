
def fact(n):
    """Compute the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * fact(n - 1)

def div(n):
    """Divide 10 by the given number n."""
    if n == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return 10 / n
