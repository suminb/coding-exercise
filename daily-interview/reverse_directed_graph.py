# [Daily Problem] Reverse a Directed Graph
#
# Hi, here's your problem today. This problem was recently asked by Facebook:
#
# Given a directed graph, reverse the directed graph so all directed edges are reversed.
#
# Example:
# Input:
# A -> B, B -> C, A ->C
#
# Output:
# B->A, C -> B, C -> A

from collections import defaultdict

import pytest


class Node:
    def __init__(self, value):
        self.adjacent = []
        self.value = value

    def __repr__(self):
        return self.value


def reverse_graph(graph):
    new_neighbors = {}
    for node in graph.values():
        new_neighbors[node.value] = []
    for node in graph.values():
        for neighbor in node.adjacent:
            new_neighbors[neighbor.value].append(node)
    for node_val, neighbors in new_neighbors.items():
        graph[node_val].adjacent = neighbors

    return graph 


# TODO: We need more comprehensive test cases
def test_reverse_graph():
    a = Node('a')
    b = Node('b')
    c = Node('c')

    a.adjacent += [b, c]
    b.adjacent += [c]

    graph = {
        a.value: a,
        b.value: b,
        c.value: c,
    }

    for node in reverse_graph(graph).values():
        print(node.value, node.adjacent)
    # a: []
    # b: ['a']
    # c: ['a', 'b']

    assert a.adjacent == []
    assert b.adjacent == [a]
    assert c.adjacent == [a, b]