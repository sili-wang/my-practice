# Definition for a N-ary node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.children = []
#
# Input type: TreeNode
# Output type: TreeNode

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = []

def subtreeMaxAvg(root: TreeNode) -> TreeNode:
    max_avg, max_avg_node = [-2 ** 64], [None]
    post_order(root, max_avg, max_avg_node)
    return max_avg_node[0]


def post_order(root, max_avg, max_avg_node):
    # BASE CASE - NULL NODE
    if not root:
        return 0, 0

    # GET THE TOTAL VALUE AND NUMBER OF NODES OF SUBTREE ROOTED AT `ROOT`
    total, num = root.val, 1

    for child in root.children:
        t, n = post_order(child, max_avg, max_avg_node)
        total += t
        num += n

    # COMPUTE THE AVERAGE
    if total / num > max_avg[0]:
        max_avg[0] = total / num
        max_avg_node[0] = root

    return total, num