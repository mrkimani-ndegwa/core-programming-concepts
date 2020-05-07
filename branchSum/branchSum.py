def cl(node, total, l):
    if node is None:
        return
    bSum = node.value + total
    if node.left is None and node.right is None:
        l.append(bSum)
        return
    cl(node.left, bSum, l)
    cl(node.right, bSum, l)


def branchSum(tree):
    total = 0
    l = []
    cl(tree, total, l)
    return l
    
    
    