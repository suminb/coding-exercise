import asyncio


async def done(result):
    return False, result, {}


async def recurse(*args, **kwargs):
    return True, args, kwargs


async def handler(f, *args, **kwargs):
    while True:
        task = asyncio.ensure_future(f(*args, **kwargs))
        recursion, args, kwargs = await task

        if not recursion:
            return args


def tail_recursion(f):
    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(handler(f, *args, **kwargs))
    return wrapper


@tail_recursion
def factorial(n, result=1):
    from trlib import done, recurse as factorial
    if n == 0:
        return done(result)
    else:
        return factorial(n - 1, result * n)


# g = globals()

# def recurse(*args, **kwargs):
#     g['@caller_id'] = (True, args, kwargs)


# def tail_recursion(f):
#     def wrapper(*args, **kwargs):
#         while True:
#             g['@caller_id'] = (False, args, kwargs)
#             res = f(*args, **kwargs)
#             recursion, args, kwargs = g['@caller_id']
#             if not recursion:
#                 return res
#     return wrapper

# import inspect

# def recurse(*args, **kwargs):
#     curr_frame = inspect.currentframe()
#     caller_frame = inspect.getouterframes(curr_frame, 2)[1]

#     import sys
#     import pdb; pdb.set_trace()

#     g['@' + caller_frame.function] = (True, args, kwargs)


# def tail_recursion(f):
#     def wrapper(*args, **kwargs):
#         caller_id = '@' + f.__name__
#         while True:
#             g[caller_id] = (False, args, kwargs)
#             res = f(*args, **kwargs)
#             recursion, args, kwargs = g[caller_id]
#             if not recursion:
#                 return res
#     return wrapper


##################

# class Recursion(Exception):
#     def __init__(self, *args, **kwargs):
#         self.args = args
#         self.kwargs = kwargs


# def recurse(*args, **kwargs):
#     raise Recursion(*args, **kwargs)


# def tail_recursion(f):
#     def wrapper(*args, **kwargs):
#         while True:
#             try:
#                 return f(*args, **kwargs)
#             except Recursion as r:
#                 args = r.args
#                 kwargs = r.kwargs
#     return wrapper
