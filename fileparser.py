"""
File parser for knapsack problems
"""

def fileparser(filename):
    item=[]
    weight=[]
    with open(filename, 'r') as f:
        numberofitems, maxweight = f.readline().split(" ").
        for line in f:
            item.append(line.split(" ")[0])
            weight.append(line.split(" ")[1])
    return numberofitems, maxweight, item, weight