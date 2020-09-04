"""
File parser for knapsack problems
"""

def fileparser(filename):
    """ parses a knapsack brolem instance file.
    Args:  
        filename: A file
    Returns:
        numberofitems: the number of items
        maxweight: the maximum weight of the knapsack
        item: a list with the profit of every item
        weight: a list with the weight of every item
    """
    item=[]
    weight=[]
    with open(filename, 'r') as f:
        numberofitems, maxweight = f.readline().split(" ")
        for line in f:
            item.append(line.split(" ")[0])
            weight.append(line.split(" ")[1])
    return numberofitems, maxweight, item, weight