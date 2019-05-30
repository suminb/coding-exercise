# Former Coding Interview Question: Compression and Decompression
# https://techdevguide.withgoogle.com/resources/compress-decompression/?types=coding-interview-question#!

import pytest


class Node:
    def __init__(self, value, children=None):
        if children is None:
            children = []
        self.value = value
        self.children = children

    def add_child(self, node):
        self.children.append(node)

    def __str__(self):
        if is_digit(self.value):
            return ''.join([str(c) for c in self.children]) * int(self.value)
        elif is_alpha(self.value):
            return self.value

    def __repr__(self):
        """For debugging purposes..."""
        return f'Node<{self.value}>'


def decompress(compressed):
    """NOTE: Assumes that inputs are always valid."""
    head = node = Node('1')
    stack = [head]
    for token in tokenize(compressed):
        if is_digit(token):
            node = Node(token)
        elif is_alpha(token):
            node = Node(token)
            stack[-1].add_child(node)
        elif token == '[':
            stack[-1].add_child(node)
            stack.append(node)
        elif token == ']':
            node = stack.pop()

    return str(head)


def is_digit(token):
    return token[0].isdigit()


def is_alpha(token):
    return token[0].isalpha()


def tokenize(characters):
    token_buf = []
    for c in characters:
        if c.isdigit():
            token_buf.append(c)
        elif c.islower():
            token_buf.append(c)
        elif c in '[]':
            yield ''.join(token_buf)
            token_buf = []
            yield c
        else:
            raise ValueError(f'Invalid input: {c}')
    if token_buf:
        yield ''.join(token_buf)


@pytest.mark.parametrize('compressed, expected', [
    ('', ''),
    ('10[a]', 'aaaaaaaaaa'),
    ('3[abc]4[ab]c', 'abcabcabcababababc'),
    ('2[3[a]b]', 'aaabaaab'),
])
def test_decompress(compressed, expected):
    actual = decompress(compressed)
    assert expected == actual


if __name__ == '__main__':
    pytest.main(['-v', __file__])