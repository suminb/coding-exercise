# 23. Merge k Sorted Lists
# difficulty: hard
# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List

import pytest

from leetcode import build_linked_list, ListNode, TreeNode


class MinHeap:
    inf = float('inf')

    def __init__(self, capacity=16):
        self.array = [0] * capacity
        self.size = 0
        self.capacity = capacity

    def insert(self, value):
        if self.size >= self.capacity:
            # NOTE: The heap grows but never shrinks. We might want to think
            # about this at some point...
            self._double_capacity()
        self.array[self.size] = value
        self._heapify(self.size)
        self.size += 1

    def pop_min(self):
        if self.size <= 0:
            raise IndexError('Cannot pop from heap of zero size')
        res = self.array[0]
        self.array[0] = self.inf
        self.size -= 1
        if self.size > 0:
            self._swap(0, self.size)
            k = 0
            while k < self.size // 2:
                l, r = self._left_child(k), self._right_child(k)
                curr, left, right = self.array[k], self.array[l], self.array[r]
                if min(left, right) < curr:
                    if left < right:
                        self._swap(l, k)
                        k = l
                    else:
                        self._swap(r, k)
                        k = r
                else:
                    break
        return res

    def _heapify(self, i):
        curr = i
        parent = self._parent(curr)
        while parent >= 0:
            if self.array[curr] < self.array[parent]:
                self._swap(curr, parent)
            curr = parent
            parent = self._parent(curr)

    def _double_capacity(self):
        self.array.extend([0] * self.capacity)
        self.capacity *= 2

    def _swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return i * 2 + 1

    def _right_child(self, i):
        return i * 2 + 2

    def _is_leaf(self, i):
        return (self.size // 2) <= i < self.size


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = MinHeap()
        for ls in lists:
            build_min_heap(heap, ls)

        if heap.size <= 0:
            return None

        head = node = ListNode(heap.pop_min())
        while heap.size > 0:
            node.next = ListNode(heap.pop_min())
            node = node.next
        return head


def build_min_heap(heap: MinHeap, list_node: ListNode) -> TreeNode:
    while list_node is not None:
        heap.insert(list_node.val)
        list_node = list_node.next


def test_merge_k_lists():
    from leetcode import assert_linked_list
    lists = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6]),
    ]
    s = Solution()
    head = s.mergeKLists(lists)
    assert_linked_list(head, [1, 1, 2, 3, 4, 4, 5, 6])


if __name__ == '__main__':
    pytest.main(['-v', __file__])