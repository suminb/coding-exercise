LeetCode
========

[LeetCode](https://leetcode.com/) is a platform to exercise algorithm problems.
Given that most people don't implement algorithms themselves in their regular
daily job, it is a good way to keep your computer science fundamentals crisp
and sharp.

### Important Notes

One thing I don't really understand is that LeetCode provides a solution
template for Python as follows:

```python
class Solution:
    def solution(self, x, y, z):
        pass
```

The class seems completely unnecessary, where a simple function would have been
sufficient.

```python
def solution(x, y, z):
    pass
```

Throughout this repository, you may find `Solution` class acts as a simple
wrapper to call another function. This makes it a bit easier to test the code
and to call other functions without `self` keyword.

```python
class Solution:
    def solution(self, x, y, z):
        return real_solution(x, y, z)

def real_solution(x, y, z):
    pass
```

### TODO

- Rename `common.py` to `leetcode.py` (or perhaps `__init__.py`)
- Use underscores rather than hyphens in `.py` files
