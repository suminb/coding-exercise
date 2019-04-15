import timeit


recursive_code = """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(n)
"""

tail_recursive_code = """
def factorial(n, result=1):
    if n == 0:
        return result
    else:
        return factorial(n - 1, result * n)

factorial(n)
"""

tail_recursion_eliminated_code = """
from trlib import tail_recursion

@tail_recursion
def factorial(n, result=1):
    from trlib import done, recurse as factorial
    if n == 0:
        return done(result)
    else:
        return factorial(n - 1, result * n)

factorial(n)
"""

number = 10000
for varname in ('recursive_code', 'tail_recursive_code',
                'tail_recursion_eliminated_code'):
    statement = globals()[varname]
    timer = timeit.Timer(stmt=statement, setup='n = 800')
    time = timer.timeit(number=number)
    print(varname)
    print('{:.3f} ms/pass\n'.format(time / number * 1000))
