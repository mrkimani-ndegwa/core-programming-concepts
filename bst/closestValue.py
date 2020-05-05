def closestValue(tree, target):
    return recurs(tree, target, float("inf"))

def recurs(t, target, closestVal):
    if t is None:
        return closestVal
    if abs(target - closestVal) > abs(target - t.value):
        closestVal = t.value
    if(target < t.value):
        return recurs(t.left, target, closestVal)
    elif (target > t.value):
        return recurs(t.right, target, closestVal)
    else:
        return closestVal

    
