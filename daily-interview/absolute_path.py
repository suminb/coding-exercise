# [Daily Problem] Absolute Path
#
# Given a file path with folder names, '..' (Parent directory), and '.'
# (Current directory), return the shortest possible file path (Eliminate all
# the '..' and '.').
#
# Example
# Input: '/Users/Joma/Documents/../Desktop/./../'
# Output: '/Users/Joma/'
# def shortest_path(file_path):
#   # Fill this in.
#
# print shortest_path('/Users/Joma/Documents/../Desktop/./../')
# # /Users/Joma/

import pytest


def absolute_path(file_path):
    stack = []
    elements = file_path.split("/")
    for element in elements:
        # This may fail with invalid paths.
        if element == "..":
            stack.pop()
        elif element == ".":
            pass
        else:
            stack.append(element)

    path = "/".join(stack)
    if path == "":
        return "/"
    else:
        return path


@pytest.mark.parametrize("file_path, expected", [
    ("/", "/"),
    ("/home/..", "/"),
    ("/home/.", "/home"),
    ("/home/../etc/../usr", "/usr"),
    ("/././././.", "/"),
    ("/Users/Joma/Documents/../Desktop/./../", "/Users/Joma/"),
])
def test_absolute_path(file_path, expected):
    actual = absolute_path(file_path)
    assert expected == actual