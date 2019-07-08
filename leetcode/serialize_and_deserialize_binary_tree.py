# 297. Serialize and Deserialize Binary Tree
# difficulty: hard
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

from collections import deque

import pytest

from leetcode import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque([(0, root)])
        buf = []
        while queue:
            index, node = queue.popleft()
            if node:
                buf.append((index, str(node.val)))

                if node.left:
                    queue.append((2 * index + 1, node.left))
                if node.right:
                    queue.append((2 * index + 2, node.right))

        return ','.join('{}:{}'.format(*b) for b in buf)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        kvs = {int(k): v for k, v in [pair.split(':') for pair in data.split(',')]}
        root = self.build(kvs, 0, max(kvs.keys()))
        return root

    def build(self, values, index, n):
        if index <= n and index in values:
            node = TreeNode(values[index])
            node.left = self.build(values, 2 * index + 1, n)
            node.right = self.build(values, 2 * index + 2, n)
            return node
        else:
            return None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

@pytest.mark.parametrize('serialized', [
    '',
    '0:1',
    '0:1,2:2',
    '0:1,1:2,2:3,5:6,6:7,11:12,12:13',
    '0:1,2:2,6:3,14:4,30:5,62:6',
])
def test_serialize_and_deserialize(serialized):
    codec = Codec()
    actual = codec.serialize(codec.deserialize(serialized))
    assert serialized == actual


if __name__ == '__main__':
    pytest.main([__file__])