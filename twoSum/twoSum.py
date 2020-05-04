def twoSum(arr, targetSum):
    # takes in on empty array of distinct integers
    # create a hashmap since it has O(1) lookups
    map = {}
    for num in arr:
        difference = abs(targetSum - num)
        if difference in map:
            return [difference, num]
        else:
            map[num] = difference
    return []
