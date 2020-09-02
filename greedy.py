def greedy(items, maxWeight, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue=0.0
    totalWeight = 0.0
    for i in range(len(itemsCopy)):
        if totalWeight + itemsCopy[i].getWeight() <= maxWeight:
            result.append(itemsCopy[i])
            totalValue += itemsCopy[i].getValue()
            totalWeight += itemsCopy[i].getWeight()
    return result,totalValue