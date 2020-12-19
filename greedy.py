""" the greedy function """
def greedy(items, maxWeight, keyFunction):
    """ greedy algorithm to solve knapsack problem
    Args:
        items: a list of items
        maxWeight: the max amount of weight
        keyFunction: the function to use for calculation
    Return:
        result: the items of the solution
        totalValue: the total value of the solution
    """
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue = 0.0
    totalWeight = 0.0
    for i in range(len(itemsCopy)):
        if totalWeight + itemsCopy[i].getWeight() <= maxWeight:
            result.append(itemsCopy[i])
            totalValue += itemsCopy[i].getValue()
            totalWeight += itemsCopy[i].getWeight()
    return result, totalValue