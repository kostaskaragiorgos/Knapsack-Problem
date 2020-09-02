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
