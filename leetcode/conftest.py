from pytest import fixture

from leetcode import build_binary_tree as build_binary_tree_, TreeNode


@fixture
def assert_list_equals():
    def func(xs, ys):
        assert set(tuple([tuple(x) for x in xs])) == set(tuple([tuple(y) for y in ys]))
    return func


@fixture
def build_binary_tree():
    return build_binary_tree_
