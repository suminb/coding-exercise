from trlib import tail_recursion


@tail_recursion
def factorial(n, result=1):
    from trlib import done, recurse as factorial
    if n == 0:
        return done(result)
    else:
        return factorial(n - 1, result * n)

print(factorial(2000))
