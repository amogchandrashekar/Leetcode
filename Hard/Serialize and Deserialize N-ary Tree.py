class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def serialize(self, root):
        res = []

        def dfs(node):
            res.append(str(node.label))
            for child_node in node.neighbors:
                dfs(child_node)
            res.append("N")

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        nodes = data.split(',')
        stack = []

        for node in nodes:
            if node != "N":
                stack.append(DirectedGraphNode(int(node)))
            else:
                child_node = stack.pop()

                if stack:
                    stack[-1].neighbors.append(child_node)
                else:
                    return child_node


if __name__ == '__main__':
    root = DirectedGraphNode(1)
    node1 = DirectedGraphNode(3)
    node2 = DirectedGraphNode(2)
    node3 = DirectedGraphNode(4)
    root.neighbors.append(node1)
    root.neighbors.append(node2)
    root.neighbors.append(node3)

    serialized = Solution().serialize(root)
    deserialized = Solution().deserialize(serialized)
    print(deserialized == root)
