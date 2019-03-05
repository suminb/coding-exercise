from pytest import fixture


@fixture
def assert_list_equals():
    def func(xs, ys):
        assert set(tuple([tuple(x) for x in xs])) == set(tuple([tuple(y) for y in ys]))
    return func
