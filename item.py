class Item:
    """
    A class to represent an item.
    '''
    Attributes
    ----------
    name  : str
        the name of the item
    value : float
        the value of the item
    weight : float
        the weight of the item

    Methods
    -------
    getName()
    getValue()
    getWeight()
    """
    def __init__(self, name, value, weight):
        """
        Constructs all the necessary attributes for the item object.

        Parameters
        ----------
            name  : str
                then name of the item
            value : float
                the value of the item
            weight : float
                the weight of the item
        """
        self.name = str(name)
        self.value = float(value)
        self.weight = float(weight)

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight
    
    def getName(self):
        return self.name

    def __str__(self):
        return 'Name:' + str(self.name) + 'Value:' + str(self.value) + ' Weight:' + str(self.weight)


def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()
    