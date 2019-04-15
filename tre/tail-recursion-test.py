from trlib import tail_recursion


@tail_recursion
def factorial(n, result=1):
    from trlib import recurse as factorial
    if n == 0:
        return result
    else:
        return factorial(n - 1, result * n)


def test():
    import pdb; pdb.set_trace()
    # assert factorial(1) == 1
    # assert factorial(2) == 2
    # assert factorial(3) == 6
    assert factorial(2000) > 0
