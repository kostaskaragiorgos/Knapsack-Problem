class Item(object):
    def __init__(self, value, weight):
        self.value = float(value)
        self.weight = float(weight)
    
    def getValue(self):
        return self.value
    
    def getWeight(self):
        return self.weight
    
    def __str__(self):
        return 'Value:' + str(self.value) + ' Weight:' + str(self.weight)


def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()